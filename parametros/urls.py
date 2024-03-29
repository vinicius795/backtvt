from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from parametros import views

urlpatterns = [
    path('add/', views.addparametro.as_view()),
    path('fpagamento/', views.addpagamento.as_view()),
    path('<str:parametro>', views.parametro.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
