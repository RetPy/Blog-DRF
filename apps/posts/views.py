from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import *
from .models import *
from .permissions import *


class PostAPIView(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnerPermission, IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return PostDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostImageAPIView(viewsets.ModelViewSet):

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [OwnerPermission, IsAuthenticatedOrReadOnly]


class PostVideoAPIView(viewsets.ModelViewSet):

    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer
    permission_classes = [OwnerPermission, IsAuthenticatedOrReadOnly]


class PostTagAPIView(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = PostTagSerializer
    permission_classes = [OwnerPermission, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeAPIView(generics.ListCreateAPIView):

    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
