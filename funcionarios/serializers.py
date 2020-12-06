from rest_framework import serializers
from funcionarios.models import *


class FuncionariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = FUNCIONARIOS
        fields = ['id', 'NOME', 'SOBRENOME', 'CARGO', 'USUARIO', 'SITUACAO']

    def create(self, validated_data):
        lista_cargos = validated_data.pop("CARGO")
        novo_funcionario = FUNCIONARIOS.objects.create(**validated_data)
        for x in lista_cargos:
            novo_funcionario.CARGO.add(CARGOS.objects.get(CARGO=x))
        return novo_funcionario

    def update(self, instance, validated_data):
        instance.NOME = validated_data.get('nome', instance.NOME)
        instance.SOBRENOME = validated_data.get(
            'sobrenome', instance.SOBRENOME)
        instance.CARGO = instance.validated_data.get('cargo', instance.CARGO)
        instance.USUARIO = instance.validated_data.get(
            'usuario', instance.USUARIO)
        instance.SITUACAO = instance.validated_data.get(
            'situacao', instance.SITUACAO)
        return instance


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CARGOS
        fields = ['id', 'CARGO']

    def create(self, validated_data):
        return CARGOS.objects.create(**validated_data)
