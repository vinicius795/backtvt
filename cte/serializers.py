from rest_framework import serializers
from cte.models import *
from datetime import datetime
from parametros.models import Parametros
from django.core.exceptions import ObjectDoesNotExist

class CTESerializer(serializers.ModelSerializer):
    class Meta:
        model = CTE
        fields = ['id', 'NR_DACTE', 'REMETENTE', 'DESTINATARIO', 'NR_CONTROLE', 'VALOR', 'VOLUMES', 'NFE']

    def create(self, validated_data):
        return CTE.objects.create(**validated_data)
        


""""

{'NR_DACTE': '4121048942366900176757001000050945100270989', 'REMETENTE': 'VENNER LUMBER DO BRASIL LTDA', 'DESTINATARIO': 'PIU MOBILE ESTF LTDA', 'NR_CONTROLE': 'CTB167669-5', 'VALOR': Decimal('90.78'), 'VOLUMES': '1', 'NFE': '000002876'}
{
    'NR_DACTE': '41201189423669001767570010000495291002695678',
    Chave CTe: "41171289423669001767570010000365921002428842�"

    'REMETENTE': 'TESTE',
    Cliente Remetente: "PROFILGLASS DO BRASIL IMP. E E"
    
    'DESTINATARIO': 'TESTE',
    Cliente Destinatario: "VILACOS IMPLEMENTOS RODOVIARIOS E AGRICOLAS EIRELI"
    
    'NR_CONTROLE': 'ABC-1234567',
    CTRC: "CTB153295-2"
    
    'VALOR': 123.45,
    Valor do Frete: "        873,06"
    
    
    'VOLUMES': '5',
    
    
    'NFE': '123456/456789'
}


"↵1": "↵2"

Chave CTe: "41171289423669001767570010000365921002428842�"
Cliente Destinatario: "VILACOS IMPLEMENTOS RODOVIARIOS E AGRICOLAS EIRELI"
Cliente Remetente: "PROFILGLASS DO BRASIL IMP. E E"
Numero CT-e: "001000036592"
Numero de Controle: " 0000000000000"
Valor do Frete: "        873,06"
"""
