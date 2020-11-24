from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cte import views

urlpatterns = [
    path('<int:CTE>/', views.CTEDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
