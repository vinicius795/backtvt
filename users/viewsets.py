from django.contrib.auth.models import User

from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly

from .models import Profile

from users.serializers import ProfileSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOwnerOrGetAndPostOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = (IsProfileOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
