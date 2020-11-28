from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from cte import views

urlpatterns = [
    path('<int:CTE>/', views.CTEDetail.as_view()),
    path('updatesp/', views.AddCTE.as_view()),
    re_path(r'^upload/(?P<filename>[^/]+)$', views.AddCTE.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
