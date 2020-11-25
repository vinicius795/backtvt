from django.urls import path, include

urlpatterns = [
    path('api/cte/', include('cte.urls')),
    path('api/funcionarios/', include('funcionarios.urls')),
    path('api/relatorios/', include('relatorios.urls')),
    path('api/parametros/', include('parametros.urls')),
]
