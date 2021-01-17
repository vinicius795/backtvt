from rest_framework import generics
from relatorios.models import *
from relatorios.serializers import *


class EntregaDetail(generics.RetrieveUpdateAPIView):
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaRetrieveSerializer

class EntregaSave(generics.CreateAPIView):
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaCreateSerializer

class EntregaList(generics.ListAPIView):
    queryset = ENTREGA.objects.all()
    serializer_class = EntregaListSerializer