from django.db import models
from django.contrib.auth.models import User
from funcionarios.models import FUNCIONARIOS, VEICULOS


class ENTREGA(models.Model):

    USUARIO = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    VEICULOS = models.ForeignKey(VEICULOS, on_delete=models.DO_NOTHING)
    MOTORISTA = models.ForeignKey(
        FUNCIONARIOS, related_name='motorista_funcionario', on_delete=models.DO_NOTHING)
    AJUDANTE = models.ForeignKey(
        FUNCIONARIOS, related_name='ajudante_funcionario', on_delete=models.DO_NOTHING)
    OBS = models.TextField()
    DATA = models.DateTimeField(auto_now=True)
    CTE = models.TextField()

    def __str__(self):
        return self.id
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ENTREGA'
        verbose_name_plural = 'ENTREGAs'
