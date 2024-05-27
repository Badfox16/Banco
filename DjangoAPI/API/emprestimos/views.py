from django.shortcuts import redirect, render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import ApprovalForm, EmprestimoForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import aprovado, Emprestimo
from . serializers import aprovadoSerializers
import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter


class AprovadoView(viewsets.ModelViewSet):
	queryset = aprovado.objects.all()
	serializer_class = aprovadoSerializers
 
def emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'tables/emprestimos.html', {'emprestimos': emprestimos})
     
def ohevalue(df):
	ohe_col=joblib.load("C:/Users/User/Desktop/IA/Banco/DjangoAPI/API/emprestimos/allcol.pkl")
	cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	newdict={}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i]=df_processed[i].values
		else:
			newdict[i]=0
	newdf=pd.DataFrame(newdict)
	return newdf
		
#@api_view(["POST"])
def deserialize_model(model_json, model_weights):
    from keras.models import model_from_json
    model = model_from_json(model_json)
    model.set_weights(model_weights)
    return model

with open('C:/Users/User/Desktop/IA/Banco/DjangoAPI/API/emprestimos/emprestimo.pkl', 'rb') as f:
    model_json, model_weights = pickle.load(f)
    clf_carregado = deserialize_model(model_json, model_weights)
	
# Abre o arquivo scaler.pkl para leitura binária (modo 'rb')
with open('C:/Users/User/Desktop/IA/Banco/DjangoAPI/API/emprestimos/scaler.pkl', 'rb') as f:
    # Carrega o objeto scaler do arquivo usando o pickle
    scaler = pickle.load(f)

def approvereject(unit):
	try:
		mdl=clf_carregado
		# scalers=joblib.load("C:/Users/User/Desktop/IA/Banco/DjangoAPI/API/emprestimos/scaler.pkl")
		X=scaler.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.5)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Aprovado', False:'Recusado'})
		K.clear_session()
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])

def cxcontact(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            Dependents = form.cleaned_data['Dependents']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']

            # Faça a previsão do resultado do empréstimo
            myDict = request.POST.dict()
            df = pd.DataFrame(myDict, index=[0])
            resultado = approvereject(ohevalue(df))[0]

            # Crie uma instância do modelo Emprestimo e atribua os valores
            emprestimo = Emprestimo(
                firstname=Firstname,
                lastname=Lastname,
                dependents=Dependents,
                applicantIncome=ApplicantIncome,
                coapplicantIncome=CoapplicantIncome,
                loanAmount=LoanAmount,
                loan_Amount_Term=Loan_Amount_Term,
                credit_History=Credit_History,
                gender=Gender,
                married=Married,
                education=Education,
                self_Employed=Self_Employed,
                property_Area=Property_Area,
                resultado=resultado
            )

            # Salve a instância no banco de dados
            emprestimo.save()

            # Resto do código para exibir mensagens de sucesso, etc.
            Xscalers = approvereject(ohevalue(df))[1]
            if int(df['LoanAmount']) < 250000:
                messages.success(request, f'Emprestimo: {resultado}')
            else:
                messages.success(request, 'Inválido: O Valor do Emprestimo excedeu o limite de $250.000')
    else:
        form = ApprovalForm()

    return render(request, 'myform/cxform.html', {'form': form})

def detalhes(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    return render(request, 'detalhes.html', {'emprestimo': emprestimo})

def editar(request, id):
    # Carrega o objeto Emprestimo existente do banco de dados com base no ID fornecido
    emprestimo = Emprestimo.objects.get(id=id)

    if request.method == 'POST':
        # Se o formulário for submetido via POST, processa os dados conforme o código anterior
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            # Atualiza os dados do objeto Emprestimo com base nos dados do formulário
            emprestimo.firstname = form.cleaned_data['firstname']
            emprestimo.lastname = form.cleaned_data['lastname']
            emprestimo.dependents = form.cleaned_data['Dependents']
            emprestimo.applicantIncome = form.cleaned_data['ApplicantIncome']
            emprestimo.coapplicantIncome = form.cleaned_data['CoapplicantIncome']
            emprestimo.loanAmount = form.cleaned_data['LoanAmount']
            emprestimo.loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            emprestimo.credit_History = form.cleaned_data['Credit_History']
            emprestimo.gender = form.cleaned_data['Gender']
            emprestimo.married = form.cleaned_data['Married']
            emprestimo.education = form.cleaned_data['Education']
            emprestimo.self_Employed = form.cleaned_data['Self_Employed']
            emprestimo.property_Area = form.cleaned_data['Property_Area']
            
            # Salva o objeto Emprestimo atualizado no banco de dados
            emprestimo.save()

            # Faça a previsão do resultado do empréstimo com base nos novos dados (opcional)
            myDict = request.POST.dict()
            df = pd.DataFrame(myDict, index=[0])
            emprestimo.resultado = approvereject(ohevalue(df))[0]
            emprestimo.save()

            # Redireciona para a página de detalhes do empréstimo após a edição
            return redirect('detalhes', id=id)
    else:
        # Se a requisição for uma GET, carrega o formulário preenchido com os dados existentes do empréstimo
        form = EmprestimoForm(initial={
            'firstname': emprestimo.firstname,
            'lastname': emprestimo.lastname,
            'Dependents': emprestimo.dependents,
            'ApplicantIncome': emprestimo.applicantIncome,
            'CoapplicantIncome': emprestimo.coapplicantIncome,
            'LoanAmount': emprestimo.loanAmount,
            'Loan_Amount_Term': emprestimo.loan_Amount_Term,
            'Credit_History': emprestimo.credit_History,
            'Gender': emprestimo.gender,
            'Married': emprestimo.married,
            'Education': emprestimo.education,
            'Self_Employed': emprestimo.self_Employed,
            'Property_Area': emprestimo.property_Area,
        })

    return render(request, 'myform/editar.html', {'form': form, 'emprestimo': emprestimo})


    