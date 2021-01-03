from django.db import models
from django.contrib.auth.models import User

class CARGOS(models.Model):

    CARGO = models.CharField(max_length=20)

    def __str__(self):
        return self.CARGO

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CARGOS'
        verbose_name_plural = 'CARGOSs'


class FUNCIONARIOS(models.Model):

    NOME = models.CharField(max_length=255)
    SOBRENOME = models.CharField(max_length=255)
    CARGO = models.ManyToManyField(CARGOS)
    USUARIO = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    SITUACAO = models.BooleanField(default=1)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'FUNCIONARIOS'
        verbose_name_plural = 'FUNCIONARIOSs'


class VEICULOS(models.Model):

    REFERENCIA = models.CharField(max_length=255)
    MODELO = models.CharField(max_length=20)
    PLACA = models.CharField(max_length=8, blank=False, unique=True)

    def __str__(self):
        return self.PLACA
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'VEICULOS'
        verbose_name_plural = 'VEICULOSs'
