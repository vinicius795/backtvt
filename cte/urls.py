from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from cte import views

urlpatterns = [
    path('<int:NR_DACTE>/', views.CTEDetail.as_view()),
    path('add', views.AddCTE.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
