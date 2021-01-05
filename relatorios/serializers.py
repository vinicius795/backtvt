from rest_framework import serializers
from django.contrib.auth.models import User
from relatorios.models import *
from cte.models import *
from funcionarios.models import *
from parametros.models import F_PAGAMENTO
from funcionarios.serializers import CargoSerializer, FuncionariosSerializer, VeiculosSerializer
from cte.serializers import CTESerializer
from parametros.serializers import F_PAGAMENTOSerializer


class UserSerializer(serializers.ModelSerializer):



  class Meta:
      model = User
      fields = ['id', 'username']

class CTE_FPagRetrieveSerializer(serializers.ModelSerializer):
  CTE = CTESerializer()
  F_PAGAMENTO =  F_PAGAMENTOSerializer()

  class Meta:
    model = CTE_FPag
    fields = ["CTE", "F_PAGAMENTO"]

class EntregaRetrieveSerializer(serializers.ModelSerializer):

  USUARIO = UserSerializer()
  CTE_FPag = CTE_FPagRetrieveSerializer(many=True)
  FUNCIONARIOS = FuncionariosSerializer(many = True)
  VEICULO = VeiculosSerializer()

  class Meta:
      model = ENTREGA
      fields = [
          'id',
          'USUARIO',
          'VEICULO',
          'FUNCIONARIOS',
          'OBS',
          'DATA',
          'CTE_FPag'
      ]

class CTE_FPagSerializer(serializers.ModelSerializer):

  class Meta:
    model = CTE_FPag
    fields = ["CTE", "F_PAGAMENTO"]

class EntregaCreateSerializer(serializers.ModelSerializer):

    CTE_FPag = CTE_FPagSerializer(many= True)

    class Meta:
        model = ENTREGA
        fields = [
          'id',
          'USUARIO',
          'VEICULO',
          'FUNCIONARIOS',
          'OBS',
          'DATA',
          'CTE_FPag'
          ]

    def create(self, validated_data):
      lista_cte = validated_data.pop('CTE_FPag')
      lista_func = validated_data.pop('FUNCIONARIOS')
      novo_relatorio = ENTREGA.objects.create(**validated_data)
      for x in lista_func:
        novo_relatorio.FUNCIONARIOS.add(FUNCIONARIOS.objects.get(pk=x.id))
      for x in lista_cte:
        n_ctefpag = CTE_FPag.objects.create(
          CTE = CTE.objects.get(pk=list(x.items())[0][1].id),
          F_PAGAMENTO = F_PAGAMENTO.objects.get(pk=list(x.items())[1][1].id)
          )
        novo_relatorio.CTE_FPag.add(n_ctefpag)
      return novo_relatorio
      
    def update(self, instance, validated_data):
        pass

class EntregaListSerializer(serializers.ModelSerializer):
  USUARIO = UserSerializer()
  class Meta:
    model = ENTREGA
    fields = ["id", 'USUARIO', "DATA"]


{
    "USUARIO": 1,
    "VEICULO": 1,
    "FUNCIONARIOS": [3, 5],
    "OBS": "teste",
    "CTE_FPag": [{"CTE": 999, "F_PAGAMENTO": 1}, {"CTE": 998, "F_PAGAMENTO": 1}, {"CTE": 997, "F_PAGAMENTO": 1}]
}
