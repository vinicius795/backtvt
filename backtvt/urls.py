from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserAPIView

admin_patterns = [
    path('', admin.site.urls)
]

auth_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

api_url_patterns = [
    path('cte/', include('cte.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('parametros/', include('parametros.urls')),
    path('user/', UserAPIView.as_view(), name='user'),
    path('login/', include(auth_patterns)),
]

urlpatterns = [
    path('login/', include(auth_patterns)),
    path('admin/', include(admin_patterns)),
    path('api/', include(api_url_patterns))

]
