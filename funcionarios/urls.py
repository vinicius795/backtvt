from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from funcionarios import views

urlpatterns = [
    path('', views.FuncionariosList.as_view()),
    path('novo/', views.FuncionariosCreate.as_view()),
    path('cargos/', views.CargosList.as_view()),
    path('cargos/add/', views.CargosAdd.as_view()),
    path('cargos/<str:cargo>', views.FuncionariosList.as_view()),
    path('id/<int:pk>', views.FuncionariosDetail.as_view()),
    path('id/<int:pk>/update', views.FuncionariosuUpdate.as_view()),
    path('veiculos/', views.VeiculosList.as_view()),
    path('veiculos/edit/<int:pk>', views.VeiculosEdit.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
