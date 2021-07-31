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
        fields = ['parametro', 'valor']


class F_PAGAMENTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_PAGAMENTO
        fields = ["id", "metodo"]
