from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserAPIView

urlpatterns = [
    path('api/cte/', include('cte.urls')),
    path('api/funcionarios/', include('funcionarios.urls')),
    path('api/relatorios/', include('relatorios.urls')),
    path('api/parametros/', include('parametros.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserAPIView.as_view(), name='user'),
]
