from django.shortcuts import render
from parametros.serializers import *
from parametros.models import *

from rest_framework import generics


class parametro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parametros.objects.all()
    serializer_class = ParametrosSerializer
    lookup_field = 'parametro'
