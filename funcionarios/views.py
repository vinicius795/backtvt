from rest_framework import generics
from funcionarios.models import *
from funcionarios.serializers import *


class FuncionariosList(generics.ListCreateAPIView):
    pass


class FuncionariosDetail(generics.RetrieveUpdateDestroyAPIView):
    pass


class CargosList(generics.ListCreateAPIView):
    pass
