from rest_framework import generics
from relatorios.models import *
from relatorios.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from relatorios.funcoes import checknotfound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json

class EntregaDetail(generics.RetrieveUpdateAPIView):
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaRetrieveSerializer

class EntregaSave(generics.CreateAPIView):
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaCreateSerializer

class EntregaList(generics.ListAPIView):
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaListSerializer

@api_view(['GET', 'POST', 'UPDATE'])
def missingcte(request):
    if request.method == 'POST':
        relatorio = ENTREGA.objects.get(pk=request.data['rel_id'])
        for x in request.data['ctes']:
            try:
                ctenf = CTENotFound(
                    cte = x["CTE"],
                    F_PAGAMENTO =  F_PAGAMENTO.objects.get(pk = x["F_PAGAMENTO"])
                )
                ctenf.save()
                ctenf.relatorio.add(relatorio)
            except:
                pass
        return Response({})
    if request.method == 'GET':
        return Response(checknotfound())
