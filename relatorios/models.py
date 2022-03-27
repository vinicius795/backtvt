from django.db import models
from django.contrib.auth.models import User
from funcionarios.models import CARGOS, FUNCIONARIOS, VEICULOS
from cte.models import CTE
from parametros.models import F_PAGAMENTO
import datetime

class Alteracoes(models.Model):
    alteracao = models.TextField()

class CTE_FPag(models.Model):
    CTE = models.ForeignKey(CTE, on_delete=models.DO_NOTHING)
    F_PAGAMENTO = models.ForeignKey(F_PAGAMENTO, on_delete=models.DO_NOTHING)

class FuncaoFUNCIONARIOS(models.Model):
    FUNCIONARIO = models.ForeignKey(FUNCIONARIOS, on_delete=models.DO_NOTHING, default="")
    FUNCAO = models.ForeignKey(CARGOS, on_delete=models.DO_NOTHING)

class ENTREGA(models.Model):

    USUARIO = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user")
    VEICULO = models.ForeignKey(VEICULOS, on_delete=models.DO_NOTHING)
    FUNCIONARIOS = models.ManyToManyField(FuncaoFUNCIONARIOS)
    OBS = models.TextField(blank=True, default='', null=True)
    DATA = models.DateTimeField(auto_now_add=True)
    CTE_FPag = models.ManyToManyField(CTE_FPag, blank=True)
    ALTERACAO = models.ManyToManyField(Alteracoes, blank=True)
    printable = models.BooleanField(default=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    who_close = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="wclose")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ENTREGA'
        verbose_name_plural = 'ENTREGAs'

class CTENotFound(models.Model):
    
    relatorio = models.ManyToManyField(ENTREGA)
    cte = models.CharField(max_length=44, unique=True)
    F_PAGAMENTO = models.ForeignKey(F_PAGAMENTO, on_delete=models.DO_NOTHING, default=1)
