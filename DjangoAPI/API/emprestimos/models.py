from django.db import models

# Create your models here.
class aprovado(models.Model):
	GENDER_CHOICES = (
        ('Male', 'Masculino'),
        ('Female', 'Feminino')
	)
	MARRIED_CHOICES = (
        ('Yes', 'Sim'),
        ('No', 'Não')
	)
	GRADUATED_CHOICES = (
        ('Graduate', 'Graduado'),
        ('Not_Graduate', 'Não Graduado')
	)
	SELFEMPLOYED_CHOICES = (
        ('Yes', 'Sim'),
        ('No', 'Não')
	)
	PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurbano'),
        ('Urban', 'Urbano')
	)
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	dependants=models.IntegerField(default=0)
	applicantincome=models.IntegerField(default=0)
	coapplicatincome=models.IntegerField(default=0)
	loanamt=models.IntegerField(default=0)
	loanterm=models.IntegerField(default=0)
	credithistory=models.IntegerField(default=0)
	gender=models.CharField(max_length=50, choices=GENDER_CHOICES)
	married=models.CharField(max_length=50, choices=MARRIED_CHOICES)
	graduatededucation=models.CharField(max_length=50, choices=GRADUATED_CHOICES)
	selfemployed=models.CharField(max_length=50, choices=SELFEMPLOYED_CHOICES)
	area=models.CharField(max_length=50, choices=PROPERTY_CHOICES)

	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)

class Emprestimo(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependents = models.IntegerField()
    applicantIncome = models.IntegerField()
    coapplicantIncome = models.IntegerField()
    loanAmount = models.IntegerField()
    loan_Amount_Term = models.IntegerField()
    credit_History = models.IntegerField()
    gender = models.CharField(max_length=10)
    married = models.CharField(max_length=3)
    education = models.CharField(max_length=20)
    self_Employed = models.CharField(max_length=3)
    property_Area = models.CharField(max_length=10)
    resultado = models.CharField(max_length=10)
