from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from search import viewset


urlpatterns = [
    path("<str:search>", viewset.SearchViewset.as_view({'get': 'list'})),
]
urlpatterns = format_suffix_patterns(urlpatterns)
