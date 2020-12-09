from cte.models import *
from cte.serializers import *

from parametros.models import Parametros

from datetime import datetime

import dbf
import os


def updatesp():
    try:
        os.system(
            "mount - t cifs // 10.1.1.20/db / mnt/servidor/db - o username=eneida2, password=ca*3ki, vers='1.0'")
    except:
        pass 
    serializer_class = CTESerializer()
    #table = DBF("/mnt/servidor/db/CONHEC.dbf", encoding="charmap")
    table = dbf.Table(filename="D:/tvt/CONHEC.dbf")
    table.open()
    first = len(table)-100
    last = len(table)
    n_registros = 0
    #for record, x in zip(table, range(200)):
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
    print(lastsincsp.valor)
    lastsincsp.save()
