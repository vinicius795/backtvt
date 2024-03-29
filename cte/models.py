from django.db import models
from django.db.utils import IntegrityError

class CTE(models.Model):

    NR_DACTE = models.CharField(max_length=44, unique=True)
    REMETENTE = models.CharField(max_length=255)
    DESTINATARIO = models.CharField(max_length=255)
    NR_CONTROLE = models.CharField(max_length=12)
    VALOR = models.DecimalField(max_digits=11, decimal_places=2)
    VOLUMES = models.CharField(max_length=10)
    NFE = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_dispatch = models.DateTimeField(blank=True, null=True)
    date_delivered = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CTE'
        verbose_name_plural = 'CTEs'



class Addcte:

    def __init__(self, cte, remetente, destinatario, nrcontrole, valor, nfe):
        try:
            CTE(
                NR_DACTE=cte,
                REMETENTE=remetente,
                DESTINATARIO=destinatario,
                NR_CONTROLE=nrcontrole,
                VALOR=valor,
                NFE=nfe,
            ).save()
        except IntegrityError:
            pass
