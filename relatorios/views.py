from rest_framework import generics
from relatorios.models import *
from relatorios.serializers import *


class EntregaDetail(generics.RetrieveUpdateDestroyAPIView):
    pass
