from rest_framework import viewsets

from apps.users.serializers import UserSerializer
from apps.users.models import User


class UserAPIView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer