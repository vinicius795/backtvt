from cte.models import *
from cte.serializers import *

from rest_framework import generics


class CTEDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTE.objects.all()
    serializers_class = 1
    pass
