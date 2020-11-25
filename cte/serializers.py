from rest_framework import serializers
from cte.models import *

class CTESerializer(serializers.ModelSerializer):
    class Meta:
        model = CTE
        fields = ['id', 'NR_DACTE', 'REMETENTE', 'DESTINATARIO', 'NR_CONTROLE', 'VALOR', 'VOLUMES', 'NFE']
    
    def create(self, validated_data):
        return CTE.objects.create(**validated_data)