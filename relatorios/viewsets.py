from rest_framework.decorators import permission_classes
from relatorios.models import ENTREGA
from relatorios.serializers import EntregaListSerializer, OpenReports
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

class Close_Report(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, AllowAny)
    queryset = ENTREGA.objects.filter(date_closed__isnull = True)
    serializer_class = OpenReports