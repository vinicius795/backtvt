from rest_framework import serializers
from parametros.models import *

class ParametrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametros
        fields = ['id', 'parametro', 'valor']

    def create(self, validated_data):
        return Parametros.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.valor = validated_data.get("valor", instance.valor)
        return instance

class F_PAGAMENTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_PAGAMENTO
        fields = ["id", "metodo"]