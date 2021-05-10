from django.db import models
from django.contrib.auth.models import User
from funcionarios.models import CARGOS, FUNCIONARIOS, VEICULOS
from cte.models import CTE
from parametros.models import F_PAGAMENTO

class Alteracoes(models.Model):
    alteracao = models.TextField()

class CTE_FPag(models.Model):
    CTE = models.ForeignKey(CTE, on_delete=models.DO_NOTHING)
    F_PAGAMENTO = models.ForeignKey(F_PAGAMENTO, on_delete=models.DO_NOTHING)

class FuncaoFUNCIONARIOS(models.Model):
    FUNCIONARIO = models.ForeignKey(FUNCIONARIOS, on_delete=models.DO_NOTHING, default="")
    FUNCAO = models.ForeignKey(CARGOS, on_delete=models.DO_NOTHING)

class ENTREGA(models.Model):

    USUARIO = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    VEICULO = models.ForeignKey(VEICULOS, on_delete=models.DO_NOTHING)
    FUNCIONARIOS = models.ManyToManyField(FuncaoFUNCIONARIOS)
    OBS = models.TextField(blank=True, default='', null=True)
    DATA = models.DateTimeField(auto_now=True)
    CTE_FPag = models.ManyToManyField(CTE_FPag)
    ALTERACAO = models.ManyToManyField(Alteracoes, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ENTREGA'
        verbose_name_plural = 'ENTREGAs'
