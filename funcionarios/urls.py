from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from funcionarios import views

urlpatterns = [
    path('', views.FuncionariosList.as_view()),
    path('<int:pk>', views.FuncionariosDetail.as_view()),
    path('cargos/', views.CargosList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)