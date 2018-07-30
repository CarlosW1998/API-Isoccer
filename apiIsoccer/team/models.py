from django.db import models

# Create your models here.
class employee(models.Model) :
    function = models.CharField(max_length = 50)
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 20)
    tel = models.CharField(max_length = 15)
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    aditional = models.CharField(max_length = 100, null = True)

class fans(models.Model) :
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 20)
    adress = models.CharField(max_length = 200)
    value = models.DecimalField(max_digits=6, decimal_places=2)

class recourse(models.Model) :
    Type = models.CharField(max_length = 50)
    max_ocupation = models.IntegerField()
    wc = models.IntegerField(null=True)
    lanch = models.IntegerField(null=True)

