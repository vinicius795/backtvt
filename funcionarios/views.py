from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from funcionarios.models import *
from funcionarios.serializers import *


class FuncionariosList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerList

    def list(self, request, cargo=""):
        if cargo:
            queryset = FUNCIONARIOS.objects.filter(
                CARGO__id=CARGOS.objects.get(CARGO__icontains=cargo).id, SITUACAO=1)
        elif cargo == "":
            queryset = FUNCIONARIOS.objects.all()
        serializer = FuncionariosSerializerList(queryset, many=True)
        return Response(serializer.data)

class FuncionariosDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerList

class FuncionariosCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializerAdd

class CargosList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CARGOS.objects.all()
    serializer_class = CargoSerializer

class VeiculosList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = VEICULOS.objects.all()
    serializer_class = VeiculosSerializer
