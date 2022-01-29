from rest_framework import viewsets

from .serializers import CommentSerializer
from .models import Comment
from apps.posts.permissions import OwnerPermission


class CommentAPIView(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [OwnerPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
