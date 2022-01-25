from rest_framework import viewsets

from .serializers import CommentSerializer
from .models import Comment


class CommentAPIView(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
