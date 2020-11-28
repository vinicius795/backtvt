from cte.models import *
from cte.serializers import *


from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

import dbf
import csv
import io
import os



class CTEDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTE.objects.all()
    serializers_class = CTESerializer

class AddCTE(APIView):
    def __init__(self, *args, **kwargs):
        super(AddCTE, self).__init__(*args, **kwargs)
    
    def post(self, request, filename, format=None):
        serializers_class = CTESerializer()
        csv_file = request.FILES['arquivossw']
        if("csv" in filename or "sswweb" in filename):
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
                dados = {
                    'NR_DACTE': x['Chave CTe'],
                    'REMETENTE': x['Cliente Remetente'],
                    'DESTINATARIO': x['Cliente Destinatario'],
                    'NR_CONTROLE': x['CTRC'],
                    'VALOR': float(x['Valor do Frete'].replace(",", ".").strip()),
                    'VOLUMES': "teste",
                    'NFE': "teste"
                }
                serializers_class.create(validated_data=dados)
            return Response(status=204)
        elif ("xml" in filename):
            pass
    
    def get(self, request, format=None):

        try:
            os.system(
                "mount - t cifs // 10.1.1.20/db / mnt/servidor/db - o username=eneida2, password=ca*3ki, vers='1.0'")
        except:
            pass

        serializers_class = CTESerializer()
        #table = DBF("/mnt/servidor/db/CONHEC.dbf", encoding="charmap")
        table = dbf.Table(filename="E:/tvt/CONHEC.dbf")
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
            serializers_class.create(validated_data=dados)
        return Response(status=204)
