from django.shortcuts import render
from parametros.serializers import *
from parametros.models import *

from rest_framework import generics


class parametro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parametros.objects.all()
    serializer_class = ParametrosSerializer
    lookup_field = 'parametro'

class addparametro(generics.ListCreateAPIView):
  queryset = Parametros.objects.all()
  serializer_class = ParametrosSerializer

class addpagamento(generics.ListCreateAPIView):
  queryset = F_PAGAMENTO.objects.all()
  serializer_class = F_PAGAMENTOSerializer