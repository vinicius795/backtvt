from django.db import router
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from relatorios import views, viewsets

app_name = 'relatorios'

router = routers.DefaultRouter()
router.register('today', viewsets.Today_reports)
router.register('unclosed', viewsets.Report_n_closed)
router.register('close', viewsets.Close_Report)

urlpatterns = [
    path('entrega/<int:pk>', views.EntregaDetail.as_view()),
    path('entrega/save', views.EntregaSave.as_view()),
    path('entrega/list', views.EntregaList.as_view()),
    path('entrega/checkmissing', views.missingcte),
    path('entrega/ctenf/add', views.missingcte),

]

urlpatterns = format_suffix_patterns(urlpatterns)
