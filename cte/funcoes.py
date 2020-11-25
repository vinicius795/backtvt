from django.db import IntegrityError
from django.http import HttpResponse
from dbfread import DBF

from cte.models import CTE

import os
import simplejson as json


def updatexml(request):
    pass


def updatecsv(request):
    csv_file = request.FILES['arquivossw']
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
        try:
            CTE(
                NR_DACTE=x['Chave CTe'],
                REMETENTE=x['Cliente Remetente'],
                DESTINATARIO=x['Cliente Destinatario'],
                NR_CONTROLE=x['CTRC'],
                VALOR=float(x['Valor do Frete'].replace(",", ".").strip()),
                NFE=x['Numero da Nota Fiscal'],
            ).save()
            n_registros += 1

        except IntegrityError:
            continue

    return HttpResponse(n_registros)


def updatedbf(request):
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
            try:
                CTE(
                    NR_DACTE=linha['DACTE'],
                    REMETENTE=linha['REM_CH'],
                    DESTINATARIO=linha['DEST_CH'],
                    NR_CONTROLE=linha['NRCONH_CH'],
                    VALOR=float(linha['TOTFRETE']),
                    NFE=linha['NF_REC'],
                ).save()
                n_registros += 1
            except IntegrityError:
                continue
    return HttpResponse(n_registros)
