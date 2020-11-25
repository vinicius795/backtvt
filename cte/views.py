from cte.models import *
from cte.serializers import *


from rest_framework import generics
from rest_framework.views import APIView

import csv
import io


class CTEDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTE.objects.all()
    serializers_class = 1

class AddCTE(APIView):
    def get()