from rest_framework import generics
from relatorios.models import *
from relatorios.serializers import *


class EntregaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ENTREGA.objects.all()
    serializers_class = EntregaSerializer