from django.urls import path, include

urlpatterns = [
    path('cte/', include('cte.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('parametros/', include('parametros.urls')),
]
