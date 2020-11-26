from rest_framework import serializers
from cte.models import *

class CTESerializer(serializers.ModelSerializer):
    class Meta:
        model = CTE
        fields = ['id', 'NR_DACTE', 'REMETENTE', 'DESTINATARIO', 'NR_CONTROLE', 'VALOR', 'VOLUMES', 'NFE']
    
    def create(self, validated_data):
        return CTE.objects.create(**validated_data)


""""
{
    'NR_DACTE': '41201189423669001767570010000495291002695678',
    'REMETENTE': 'TESTE',
    'DESTINATARIO': 'TESTE',
    'NR_CONTROLE': 'ABC-1234567',
    'VALOR': 123.45,
    'VOLUMES': '5',
    'NFE': '123456/456789'
}
"""
