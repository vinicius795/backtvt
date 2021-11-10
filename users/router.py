from rest_framework import routers

from .viewsets import UserViewSet, ProfileViewSet

from django.views.decorators.csrf import csrf_exempt


app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profile', ProfileViewSet)
