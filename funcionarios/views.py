from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from funcionarios.models import *
from funcionarios.serializers import *


class FuncionariosList(generics.ListAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerList

    def list(self, request, cargo=""):
        if cargo:
            queryset = FUNCIONARIOS.objects.filter(
                CARGO__id=CARGOS.objects.get(CARGO__icontains=cargo).id, SITUACAO=1)
        elif cargo == "":
            queryset = FUNCIONARIOS.objects.filter(SITUACAO=1)
        serializer = FuncionariosSerializerList(queryset, many=True)
        return Response(serializer.data)

class FuncionariosDetail(generics.RetrieveAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerList

class FuncionariosCreate(generics.CreateAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerAdd

class FuncionariosuUpdate(generics.UpdateAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerUpdate

class CargosList(generics.ListAPIView):
    queryset = CARGOS.objects.all()
    serializer_class = CargoSerializer

class CargosUpdate(generics.UpdateAPIView):
    queryset = CARGOS.objects.all()
    serializer_class = CargoSerializer

class CargosAdd(generics.CreateAPIView):
    queryset = CARGOS.objects.all()
    serializer_class = CargoSerializer


class VeiculosList(generics.ListCreateAPIView):
    queryset = VEICULOS.objects.all()
    serializer_class = VeiculosSerializer

    def list(self, request, *args, **kwargs):
        queryset = VEICULOS.objects.filter(status= True)
        serializer_class = VeiculosSerializer(queryset, many=True)
        return Response(serializer_class.data)


class VeiculosEdit(generics.UpdateAPIView):
    queryset = VEICULOS.objects.all()
    serializer_class = VeiculosSerializer
