from rest_framework import serializers
from django.contrib.auth.models import User
from relatorios.models import *
from cte.models import *
from parametros.models import F_PAGAMENTO
from funcionarios.serializers import FuncionariosSerializer


class CTE_FPagSerializer(serializers.ModelSerializer):

  class Meta:
    model = CTE_FPag
    fields = ["id", "CTE", "F_PAGAMENTO"]

class EntregaSerializer(serializers.ModelSerializer):

    CTE_FPag = CTE_FPagSerializer(many= True)
    class Meta:
        model = ENTREGA
        fields = ['id', 'USUARIO', 'VEICULO', 'FUNCIONARIOS' , 'OBS', 'DATA', 'CTE_FPag']

        def create(self, validated_data):
          print(validated_data)
          lista_cte = validated_data.pop('CTE_FPag')
          lista_func = validated_data.pop('FUNCIONARIOS')
          user  = validated_data.pop('USUARIO')
          novo_relatorio = ENTREGA.objects.create(**validated_data)
          novo_relatorio.USUARIO.add(User.objects.get(pk=user))
          for x in lista_func:
            novo_relatorio.FUNCIONARIOS.add(FUNCIONARIOS.objects.get(pk=x))
          for x in lista_cte:
            CTE_FPag.objects.create(novo_relatorio = novo_relatorio, **x)
          return novo_relatorio
          
        def update(self, instance, validated_data):
            pass


{
    "USUARIO": 1,
    "VEICULO": 1,
    "FUNCIONARIOS": [3,5],
    "OBS": "teste",
    "CTE_FPag": [{"CTE": 999,"F_PAGAMENTO": 1},{"CTE": 998,"F_PAGAMENTO": 1},{"CTE": 997,"F_PAGAMENTO": 1}]
}
