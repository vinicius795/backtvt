from rest_framework import serializers
from django.contrib.auth.models import User
from relatorios.models import *
from cte.models import *
from funcionarios.models import *
from parametros.models import F_PAGAMENTO
from funcionarios.serializers import FuncionariosSerializer

class func(serializers.ModelSerializer):
  class Meta:
    model = FUNCIONARIOS
    fields = ['id']

class CTE_FPagSerializer(serializers.ModelSerializer):

  class Meta:
    model = CTE_FPag
    fields = ["id", "CTE", "F_PAGAMENTO"]

class EntregaSerializer(serializers.ModelSerializer):

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
        print(x)
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


{
    "USUARIO": 1,
    "VEICULO": 1,
    "FUNCIONARIOS": [3, 5],
    "OBS": "teste",
    "CTE_FPag": [{"CTE": 999, "F_PAGAMENTO": 1}, {"CTE": 998, "F_PAGAMENTO": 1}, {"CTE": 997, "F_PAGAMENTO": 1}]
}
"""
{
  'USUARIO': < User: vinicius >, 
  'VEICULO': < VEICULOS: ABC-1234 > , 
  'OBS': 'teste', 
  'CTE_FPag': [
    OrderedDict([
      ('CTE', < CTE: CTE object (999) > ), 
      ('F_PAGAMENTO', < F_PAGAMENTO: F_PAGAMENTO object (1) > )]),
    OrderedDict([
      ('CTE', < CTE: CTE object (998) > ),
      ('F_PAGAMENTO', < F_PAGAMENTO: F_PAGAMENTO object (1) > )]), 
    OrderedDict([
      ('CTE', < CTE: CTE object (997) > ), 
      ('F_PAGAMENTO', < F_PAGAMENTO: F_PAGAMENTO object (1) > )])
    ]
  }
"""