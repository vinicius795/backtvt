from rest_framework import serializers
from django.contrib.auth.models import User
from relatorios.models import *
from cte.models import *
from funcionarios.models import *
from parametros.models import F_PAGAMENTO
from funcionarios.serializers import CargoSerializer, FuncionariosSerializerList, VeiculosSerializer
from cte.serializers import CTESerializer
from parametros.serializers import F_PAGAMENTOSerializer
from datetime import date


class FuncaoFuncionarioSerializerRetriving(serializers.ModelSerializer):
  FUNCIONARIO = FuncionariosSerializerList()
  FUNCAO = CargoSerializer()
  class Meta:
    model = FuncaoFUNCIONARIOS
    fields = ['id', 'FUNCIONARIO', 'FUNCAO']

class FuncaoFuncionarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = FuncaoFUNCIONARIOS
    fields = ['id', 'FUNCIONARIO', 'FUNCAO']

class UserSerializer(serializers.ModelSerializer):

  class Meta:
      model = User
      fields = ['id', 'username', 'first_name']

class CTE_FPagRetrieveSerializer(serializers.ModelSerializer):
  CTE = CTESerializer()
  F_PAGAMENTO =  F_PAGAMENTOSerializer()

  class Meta:
    model = CTE_FPag
    fields = ["CTE", "F_PAGAMENTO"]

class EntregaRetrieveSerializer(serializers.ModelSerializer):

  USUARIO = UserSerializer()
  CTE_FPag = CTE_FPagRetrieveSerializer(many=True)
  FUNCIONARIOS = FuncaoFuncionarioSerializerRetriving(many = True)
  VEICULO = VeiculosSerializer()

  class Meta:
      model = ENTREGA
      fields = [
          'id',
          'USUARIO',
          'VEICULO',
          'FUNCIONARIOS',
          'OBS',
          'DATA',
          'CTE_FPag'
      ]

class CTE_FPagSerializer(serializers.ModelSerializer):

  class Meta:
    model = CTE_FPag
    fields = ["CTE", "F_PAGAMENTO"]

class EntregaCreateSerializer(serializers.ModelSerializer):

    CTE_FPag = CTE_FPagSerializer(many= True)
    FUNCIONARIOS = FuncaoFuncionarioSerializer(many=True)

    class Meta:
        model = ENTREGA
        fields = [
          'id',
          'USUARIO',
          'VEICULO',
          'FUNCIONARIOS',
          'OBS',
          'DATA',
          'CTE_FPag',
          'printable'
          ]

    def create(self, validated_data):
      lista_cte = validated_data.pop('CTE_FPag')
      lista_func = validated_data.pop('FUNCIONARIOS')
      novo_relatorio = ENTREGA.objects.create(**validated_data)
      for x in lista_func:
        n_ffunc = FuncaoFUNCIONARIOS.objects.create(
            FUNCIONARIO=FUNCIONARIOS.objects.get(pk=list(x.items())[0][1].id),
            FUNCAO=CARGOS.objects.get(pk=list(x.items())[1][1].id)
        )
        novo_relatorio.FUNCIONARIOS.add(n_ffunc)
      for x in lista_cte:
        n_ctefpag = CTE_FPag.objects.create(
            CTE=CTE.objects.get(pk=list(x.items())[0][1].id),
            F_PAGAMENTO = F_PAGAMENTO.objects.get(pk=list(x.items())[1][1].id)
          )
        setctedate(CTE.objects.get(pk=list(x.items())[0][1].id), type = 1)
        novo_relatorio.CTE_FPag.add(n_ctefpag)
      return novo_relatorio
      
    def update(self, instance, validated_data):
        pass

def setctedate(cte: CTE, type):
  if type :
    cte.date_dispatch = date.today()
  else:
    cte.date_delivered = date.today()
  cte.save()

class EntregaListSerializer(serializers.ModelSerializer):
  USUARIO = UserSerializer()
  class Meta:
    model = ENTREGA
    fields = ["id", 'USUARIO', "DATA", "date_closed", "who_close"]

  def update(self, instance, validated_data):
    rel = EntregaRetrieveSerializer(ENTREGA.objects.get(pk=instance.id)).data
    for x in rel["CTE_FPag"]:
      cte = dict(x["CTE"])
      setctedate(CTE.objects.get(pk=cte["id"]), type = 0)
    return super().update(instance, validated_data)

class OpenReports(serializers.ModelSerializer):
  class Meta:
    model = ENTREGA
    fields = ['id', "date_closed"]




""" 
{
    "USUARIO": 1,
    "VEICULO": 1,
    "FUNCIONARIOS": [
      {
        "FUNCAO": 1, 
        "FUNCIONARIO":3
      }
    ],
    "OBS": "teste",
    "CTE_FPag": [
      {
        "CTE": 999, 
        "F_PAGAMENTO": 1
      }, 
      {
        "CTE": 998, 
        "F_PAGAMENTO": 2
      }, 
      {
        "CTE": 997, 
        "F_PAGAMENTO": 1
      }
    ]
}

{'id': 1488,
'USUARIO': OrderedDict([('id', 1), ('username', 'vinicius'), ('first_name', '')]),
'VEICULO': OrderedDict([('id', 4), ('REFERENCIA', 'Guincho'), ('MODELO', 'Munck'), ('PLACA', 'GKO 5718'), ('status', True)]),
'FUNCIONARIOS': [OrderedDict([('id', 2621), ('FUNCIONARIO', OrderedDict([('id', 25), ('NOME', 'Joaquim'), ('SOBRENOME', 'Filho'), ('CARGO', [OrderedDict([('id', 3), ('CARGO', 'Motorista'), ('SHOW_RELATORIO', True), ('status', True)])]), ('USUARIO', None), ('SITUACAO', True)])), ('FUNCAO', OrderedDict([('id', 3), ('CARGO', 'Motorista'), ('SHOW_RELATORIO', True), ('status', True)]))])], 'OBS': '', 'DATA': '2022-03-23T15:30:44.899360-03:00',
'CTE_FPag': [OrderedDict([
      ('CTE', OrderedDict([('id', 7688205), ('NR_DACTE', '41220389423669001767570010000535181002735717'), ('REMETENTE', 'ALUMIPLAST COM. DE METAIS LTDA'), ('DESTINATARIO', 'BRAZMAC IND E COMERCIO LTDA'), ('NR_CONTROLE', 'CTB170250-5'), ('VALOR', '103.19'), ('VOLUMES', '2'), ('NFE', '000102025'), ('date_add', '2022-03-23T15:30:45.074406-03:00'), ('date_dispatch', '2022-03-23T00:00:00-03:00'), ('date_delivered', None)])), ('F_PAGAMENTO', OrderedDict([('id', 3), ('metodo', 'A Prazo')]))])]} """