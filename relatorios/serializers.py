from rest_framework import serializers
from relatorios.models import *
from cte.models import CTE
from parâmetros.models import F_PAGAMENTO

class EntregaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ENTREGA
        fields = ['id', 'USUARIO', 'VEICULOS', 'FUNCIONARIOS' , 'OBS', 'DATA', 'CTE_FPag']

        def create(self, validated_data):
          lista_cte = validated_data.pop('CTE_FPag')
          lista_func = validated_data.pop('FUNCIONARIOS')
          novo_relatorio = ENTREGA.objects.create(**validated_data)
          for x in lista_func:
            novo_relatorio.FUNCIONARIOS.add(FUNCIONARIOS.objects.get(pk=x))
          for x in lista_cte:
            addcte_pag = CTE_FPAG.add(
              CTE = CTE.objects.get(pk=x.cte),
              F_PAGAMENTO = F_PAGAMENTO.objects.get(pk=x.pag)
             )
            addcte_pag.save() 
            novo_relatorio.CTE_FPag.add(addcte_pag)
          return novo_relatorio
          
        def update(self, instance, validated_data):
            pass