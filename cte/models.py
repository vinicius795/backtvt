from django.db import models

class DACTE(models.Model):

    NR_DACTE = models.CharField(max_length=44, unique=True)
    REMETENTE = models.CharField(max_length=255)
    DESTINATARIO = models.CharField(max_length=255)
    NR_CONTROLE = models.CharField(max_length=10)
    VALOR = models.DecimalField(max_digits=11, decimal_places=2)
    VOLUMES = models.CharField(max_length=10)
    NFE = models.TextField()

    def __str__(self):
        return self.NR_CONTROLE, self.NFE
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CTE'
        verbose_name_plural = 'CTEs'
