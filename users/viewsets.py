import json
from django.contrib.auth.models import User

from rest_framework import viewsets, mixins

from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly

from .models import Profile

from users.serializers import ProfileSerializer, UserSerializer

from django.views.decorators.csrf import csrf_exempt, requires_csrf_token


from django.utils.decorators import method_decorator


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOwnerOrGetAndPostOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = (IsProfileOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
