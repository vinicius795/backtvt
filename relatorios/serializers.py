from rest_framework import serializers
from relatorios.models import *

class EntregaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ENTREGA
        fields = ['id', 'USUARIO', 'VEICULOS', 'MOTORISTA', 'AJUDANTE', 'OBS', 'DATA', 'CTE']

        def create(self, validated_data):
            return ENTREGA.objects.create(**validated_data)

        def update(self, instance, validated_data):
            pass