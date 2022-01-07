from rest_framework.permissions import IsAdminUser, IsAuthenticated
from cte.models import CTE
from cte.serializers import CTESerializer
from rest_framework import viewsets


class Delayed_ctes(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = CTE.objects.filter(date_delivered__isnull = True)
    serializer_class = CTESerializer
