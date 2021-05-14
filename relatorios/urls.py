from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from relatorios import views

urlpatterns = [
    path('entrega/<int:pk>', views.EntregaDetail.as_view()),
    path('entrega/save', views.EntregaSave.as_view()),
    path('entrega/list', views.EntregaList.as_view()),
    path('entrega/checkmissing', views.missingcte),
    path('entrega/ctenf/add', views.missingcte),

]

urlpatterns = format_suffix_patterns(urlpatterns)
