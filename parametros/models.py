from django.db import models

class Parametros(models.Model):
    parametro = models.CharField(max_length=255, unique=True)
    valor = models.CharField(max_length=255)

class F_PAGAMENTO(models.Model):
    metodo = models.CharField(max_length=255)
