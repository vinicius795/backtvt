from relatorios.models import ENTREGA
from relatorios.serializers import EntregaListSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from datetime import date


class Today_reports(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser, AllowAny)
    queryset = ENTREGA.objects.filter(DATA__date = date.today())
    serializer_class = EntregaListSerializer

class Report_n_closed(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, AllowAny)
    queryset = ENTREGA.objects.filter(date_closed__isnull = True)
    serializer_class = EntregaListSerializer
