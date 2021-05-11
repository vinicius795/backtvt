from rest_framework import generics
from relatorios.models import *
from relatorios.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from relatorios.funcoes import checknotfound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class EntregaDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaRetrieveSerializer

class EntregaSave(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaCreateSerializer

class EntregaList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaListSerializer

class Missingcte(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        
        if request.method == 'GET':
            checknotfound()
            return Response(status=status.HTTP_200_OK)
