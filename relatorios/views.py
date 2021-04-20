from rest_framework import generics
from relatorios.models import *
from relatorios.serializers import *
from rest_framework.permissions import IsAuthenticated


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
