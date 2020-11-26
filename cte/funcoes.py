from django.db import IntegrityError
from django.http import HttpResponse
from dbfread import DBF

from cte.models import CTE

import os
import simplejson as json
import csv
import io


def updatexml(request):
    pass




def updatecsv():
    csv_file = 'arquivossw'
    cabeca = []
    lista = []
    n_registros = 0

    class espasador:
        delimiter = ';'
        quotechar = '"'
        escapechar = None
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'

    decoded_file = csv_file.read().decode('iso-8859-1')
    io_string = io.StringIO(decoded_file)
    for row in csv.reader(io_string, dialect=espasador):
        if row[0] == "1":
            cabeca = row
            cabeca.pop(len(cabeca)-1)
        if row[0] == "2":
            itens = {}
            for x in range(len(cabeca)):
                a = row
                itens[cabeca[x]] = a[x]
            lista.append(itens)

    for x in lista:
        Addcte(
            cte=x['Chave CTe'],
            remetente=x['Cliente Remetente'],
            destinatario=x['Cliente Destinatario'],
            nrcontrole=x['CTRC'],
            valor=float(x['Valor do Frete'].replace(",", ".").strip()),
            nfe=x['Numero da Nota Fiscal'],
        )
        n_registros += 1
    return HttpResponse(n_registros)


def updatedbf():
    try:
        os.system(
            "mount - t cifs // 10.1.1.20/db / mnt/servidor/db - o username=eneida2, password=ca*3ki, vers='1.0'")
    except:
        pass

    #table = DBF("/mnt/servidor/db/CONHEC.dbf", encoding="charmap")
    table = DBF("D:/tvt/CONHEC.dbf", encoding="charmap")
    n_registros = 0
    #for record, x in zip(table, range(200)):
    for record in table:
        linha = dict(record)
        if int(str(linha["NRCONH_CH"])) >= 650000:
            Addcte(
                cte=linha['DACTE'],
                remetente=linha['REM_CH'],
                destinatario=linha['DEST_CH'],
                nrcontrole=linha['NRCONH_CH'],
                valor=float(linha['TOTFRETE']),
                nfe=linha['NF_REC'],
            )
            n_registros += 1
    return HttpResponse(n_registros)

class Addcte():

    def __init__(self, tipo, arquivo):
        self.tipo = tipo
        self.dados = dados
        self.arquivo = arquivo
        self.nregistros = 0
    
    def add(self, **kwargs):
        try:
            CTE(
                NR_DACTE=kwargs.get('cte'),
                REMETENTE=kwargs.get('remetente'),
                DESTINATARIO=kwargs.get('destinatario'),
                NR_CONTROLE=kwargs.get('nrcontrole'),
                VALOR=kwargs.get('valor'),
                NFE=kwargs.get('nfe'),
            ).save()
            self.nregistros += 1
        except IntegrityError:
            pass
    
    def csv(self):
        pass

    def dbf(self):
        pass


    if (tipo == 'csv'):
        csv()
    elif (tipo == 'dbf'):
        dbf()
