from cte.models import *
from cte.serializers import *
from cte.funcoes import *

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics
from rest_framework import mixins
#from rest_framework.views import APIView
#from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

#import dbf
#import csv
#import io
#import os

class ctelist(generics.ListAPIView):
  queryset = CTE.objects.all()
  serializer_class = CTESerializer

class CTEDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTE.objects.all()
    serializer_class = CTESerializer
    def get(self, request, modo, valor):
        if ( modo == "dacte"):
            queryset = CTE.objects.get(NR_DACTE=valor)
        elif( modo == "id"):
            queryset = CTE.objects.get(pk=valor)
        serializer = CTESerializer(queryset)
        return Response(serializer.data)


class AddCTE(generics.ListCreateAPIView):
    
    queryset = CTE.objects.all()
    serializer_class = CTESerializer
    def post(self, request, *args, **kwargs):
        try:
            queryset = CTE.objects.get(
                NR_DACTE=request.data['NR_DACTE'])
            serializer = CTESerializer(queryset)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return super().post(request, *args, **kwargs)
    def list(self, request):
        try:
            updatesp()
            return Response(status=204)
        except:
            return Response(status=500)
#    
#    def arquivo(self, request, filename):
#        serializer_class = CTESerializer()
#        csv_file = request.FILES['arquivossw']
#        
#        if("csv" in filename or "sswweb" in filename):
#            cabeca = []
#            lista = []
#            n_registros = 0
#            class espasador:
#                delimiter = ';'
#                quotechar = '"'
#                escapechar = None
#                doublequote = True
#                skipinitialspace = False
#                lineterminator = '\r\n'
#
#            decoded_file = csv_file.read().decode('iso-8859-1')
#            io_string = io.StringIO(decoded_file)
#            for row in csv.reader(io_string, dialect=espasador):
#                if row[0] == "1":
#                    cabeca = row
#                    cabeca.pop(len(cabeca)-1)
#                if row[0] == "2":
#                    itens = {}
#                    for x in range(len(cabeca)):
#                        a = row
#                        itens[cabeca[x]] = a[x]
#                    lista.append(itens)
#
#            for x in lista:
#                print(x)
#                if 'Volumes' not in x:
#                    x['Volumes'] = None
#                if 'NFE' not in x:
#                    x['NFE'] = None
#                dados = {
#                    'NR_DACTE': x['Chave CTe'][0:43],
#                    'REMETENTE': x['Cliente Remetente'],
#                    'DESTINATARIO': x['Cliente Destinatario'],
#                    'NR_CONTROLE': x['CTRC'],
#                    'VALOR': float(x['Valor do Frete'].replace(",", ".").strip()),
#                    'VOLUMES': x['Volumes'],
#                    'NFE': x['NFE']
#                }
#                serializer_class.create(validated_data=dados)
#            return Response(status=204)
#        elif ("xml" in filename):
#            pass
#        
#
#
#    def list(self, request, origem, filename =""):
#        if origem == "sp":
#            try:
#                self.sp()
#                return Response(status=204)
#            except:
#                return Response(status=500)
#
#        elif origem == "file":
#            try:
#                print(request.FILES['arquivossw'])
#                self.arquivo(request, filename)
#            except:
#                return Response(status=500)
