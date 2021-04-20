from django.shortcuts import render
from parametros.serializers import *
from parametros.models import *
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics


class parametro(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Parametros.objects.all()
  serializer_class = ParametrosSerializer
  lookup_field = 'parametro'

class addparametro(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Parametros.objects.all()
  serializer_class = ParametrosSerializer

class addpagamento(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = F_PAGAMENTO.objects.all()
  serializer_class = F_PAGAMENTOSerializer
