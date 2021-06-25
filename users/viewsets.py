from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
