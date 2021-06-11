from rest_framework import serializers
from funcionarios.models import *
from parametros.serializers import UserSerializer


class VeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model =VEICULOS
        fields = ["id", 'REFERENCIA', 'MODELO', "PLACA", "status"]
    
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CARGOS
        fields = ['id', 'CARGO', 'SHOW_RELATORIO']

    def create(self, validated_data):
        return CARGOS.objects.create(**validated_data)

class CargoSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = CARGOS
        fields = ['CARGO', 'SHOW_RELATORIO']

class FuncionariosSerializerAdd(serializers.ModelSerializer):

    class Meta:
        model = FUNCIONARIOS
        fields = ['id', 'NOME', 'SOBRENOME', 'CARGO', 'USUARIO', 'SITUACAO']

    def create(self, validated_data):
        lista_cargos = validated_data.pop("CARGO")
        novo_funcionario = FUNCIONARIOS.objects.create(**validated_data)
        for x in lista_cargos:
            novo_funcionario.CARGO.add(CARGOS.objects.get(CARGO=x))
        return novo_funcionario

    """def update(self, instance, validated_data):
        instance.NOME = validated_data.get('nome', instance.NOME)
        instance.SOBRENOME = validated_data.get(
            'sobrenome', instance.SOBRENOME)
        instance.CARGO = instance.validated_data.get('cargo', instance.CARGO)
        instance.USUARIO = instance.validated_data.get(
            'usuario', instance.USUARIO)
        instance.SITUACAO = instance.validated_data.get(
            'situacao', instance.SITUACAO)
        return instance """

class FuncionariosSerializerList(serializers.ModelSerializer):

    CARGO = CargoSerializer(many=True)
    USUARIO = UserSerializer()

    class Meta:
        model = FUNCIONARIOS
        fields = ['id', 'NOME', 'SOBRENOME', 'CARGO', 'USUARIO', 'SITUACAO']


class FuncionariosSerializerUpdate(serializers.ModelSerializer):
    USUARIO = UserSerializer()

    class Meta:
        model = FUNCIONARIOS
        fields = ['id', 'NOME', 'SOBRENOME', 'CARGO', 'USUARIO', 'SITUACAO']
