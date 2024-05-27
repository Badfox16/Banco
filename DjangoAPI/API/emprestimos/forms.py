from django import forms

class ApprovalForm(forms.Form):
    firstname = forms.CharField(max_length=15, label='Nome', widget=forms.TextInput(attrs={'placeholder': 'Insira seu nome'}))
    lastname = forms.CharField(max_length=15, label='Sobrenome', widget=forms.TextInput(attrs={'placeholder': 'Insira seu sobrenome'}))
    Dependents = forms.IntegerField(label='Dependentes', widget=forms.TextInput(attrs={'placeholder': 'Número de dependentes'}))
    ApplicantIncome = forms.IntegerField(label='Renda do Solicitante', widget=forms.TextInput(attrs={'placeholder': 'Renda do solicitante em USD$'}))
    CoapplicantIncome = forms.IntegerField(label='Renda do Cônjuge', widget=forms.TextInput(attrs={'placeholder': 'Renda do cônjuge em USD$'}))
    LoanAmount = forms.IntegerField(label='Valor do Empréstimo', widget=forms.TextInput(attrs={'placeholder': 'Valor do empréstimo em USD$'}))
    Loan_Amount_Term = forms.IntegerField(label='Prazo do Empréstimo', widget=forms.TextInput(attrs={'placeholder': 'Prazo do empréstimo em meses'}))
    Credit_History=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2)], label='Histórico de Crédito')
    Gender = forms.ChoiceField(choices=[('Male', 'Masculino'), ('Female', 'Feminino')], label='Gênero', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Married = forms.ChoiceField(choices=[('Yes', 'Sim'), ('No', 'Não')], label='Casado', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Education = forms.ChoiceField(choices=[('Graduate', 'Graduado'), ('Not_Graduate', 'Não Graduado')], label='Educação', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Self_Employed = forms.ChoiceField(choices=[('Yes', 'Sim'), ('No', 'Não')], label='Autônomo', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Property_Area = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurbano'), ('Urban', 'Urbano')], label='Área de Propriedade', widget=forms.Select(attrs={'placeholder': 'Selecione'}))

class EmprestimoForm(forms.Form):
    firstname = forms.CharField(max_length=15, label='Nome', widget=forms.TextInput(attrs={'placeholder': 'Insira seu nome'}))
    lastname = forms.CharField(max_length=15, label='Sobrenome', widget=forms.TextInput(attrs={'placeholder': 'Insira seu sobrenome'}))
    Dependents = forms.IntegerField(label='Dependentes', widget=forms.TextInput(attrs={'placeholder': 'Número de dependentes'}))
    ApplicantIncome = forms.IntegerField(label='Renda do Solicitante', widget=forms.TextInput(attrs={'placeholder': 'Renda do solicitante em USD$'}))
    CoapplicantIncome = forms.IntegerField(label='Renda do Cônjuge', widget=forms.TextInput(attrs={'placeholder': 'Renda do cônjuge em USD$'}))
    LoanAmount = forms.IntegerField(label='Valor do Empréstimo', widget=forms.TextInput(attrs={'placeholder': 'Valor do empréstimo em USD$'}))
    Loan_Amount_Term = forms.IntegerField(label='Prazo do Empréstimo', widget=forms.TextInput(attrs={'placeholder': 'Prazo do empréstimo em meses'}))
    Credit_History=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2)], label='Histórico de Crédito')
    Gender = forms.ChoiceField(choices=[('Male', 'Masculino'), ('Female', 'Feminino')], label='Gênero', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Married = forms.ChoiceField(choices=[('Yes', 'Sim'), ('No', 'Não')], label='Casado', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Education = forms.ChoiceField(choices=[('Graduate', 'Graduado'), ('Not_Graduate', 'Não Graduado')], label='Educação', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Self_Employed = forms.ChoiceField(choices=[('Yes', 'Sim'), ('No', 'Não')], label='Autônomo', widget=forms.Select(attrs={'placeholder': 'Selecione'}))
    Property_Area = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurbano'), ('Urban', 'Urbano')], label='Área de Propriedade', widget=forms.Select(attrs={'placeholder': 'Selecione'}))