from rest_framework import serializers
from django.contrib.auth.models import User
from parametros.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

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
