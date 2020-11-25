from rest_framework import generics
from funcionarios.models import *
from funcionarios.serializers import *


class FuncionariosList(generics.ListCreateAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializers_class = FuncionariosSerializer


class FuncionariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializers_class = FuncionariosSerializer


class CargosList(generics.ListCreateAPIView):
    queryset = CARGOS.objects.all()
    serializers_class = FuncionariosSerializer
