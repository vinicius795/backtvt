from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from users import router as users_api_router

admin_patterns = [
    path('', admin.site.urls)
]

auth_api_urls = [
    path('', include('rest_framework_social_oauth2.urls')),
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify', include("rest_framework.urls")))

api_url_patterns = [
    path('cte/', include('cte.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('parametros/', include('parametros.urls')),
    path('search/', include('search.urls')),
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns))
]
