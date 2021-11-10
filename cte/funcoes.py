from cte.models import *
from cte.serializers import *

from parametros.models import Parametros

from relatorios.funcoes import checknotfound
from datetime import datetime


import json
import dbf
import os
import time


def updatesp():
    serializer_class = CTESerializer()
    #table = dbf.Table(filename="E:/tvt/CONHEC.dbf", codepage="cp860")
    #table = dbf.Table(filename="D:/tvt/CONHEC.dbf", codepage="cp860")
    table = dbf.Table(filename="/mnt/servidor/db/CONHEC.dbf", codepage="cp860")
    table.open()
    first = len(table)-1000
    last = len(table)
    n_registros = 0
    for linha in table[first:last]:
        dados = {
            'NR_DACTE': linha['DACTE'],
            'REMETENTE': linha['REM_CH'],
            'DESTINATARIO': linha['DEST_CH'],
            'NR_CONTROLE': linha['NRCONH_CH'],
            'VALOR': float(linha['TOTFRETE']),
            'VOLUMES': linha['QTVOL_CH'],
            'NFE': linha['NF_REC']
        }
        try:
            serializer_class.create(validated_data=dados)
        except:
            pass
    agora = datetime.now()
    lastsincsp = Parametros.objects.get(parametro="lastsincsp")
    lastsincsp.valor = str(agora.strftime("%d/%m/%Y %H:%M"))
    lastsincsp.save()
    checknotfound()
