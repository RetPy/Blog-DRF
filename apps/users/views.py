from rest_framework import viewsets

from apps.users.serializers import UserSerializer
from apps.users.models import User
from apps.posts.permissions import OwnerPermission


class UserAPIView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OwnerPermission]
