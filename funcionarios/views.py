from rest_framework import generics
from rest_framework.response import Response

from funcionarios.models import *
from funcionarios.serializers import *


class FuncionariosList(generics.ListCreateAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializer

    def list(self, request, cargo=""):
        if cargo:
            queryset = FUNCIONARIOS.objects.filter(
                CARGO__id=CARGOS.objects.get(CARGO__icontains=cargo).id, SITUACAO=1)
        elif cargo == "":
            queryset = FUNCIONARIOS.objects.all()
        serializer = FuncionariosSerializer(queryset, many=True)
        return Response(serializer.data)

class FuncionariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FUNCIONARIOS.objects.all()
    serializer_class = FuncionariosSerializer


class CargosList(generics.ListCreateAPIView):
    queryset = CARGOS.objects.all()
    serializer_class = CargoSerializer
