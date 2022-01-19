from rest_framework import viewsets, generics

from .serializers import *
from .models import *


class PostAPIView(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return PostDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostImageAPIView(viewsets.ModelViewSet):

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


class PostVideoAPIView(viewsets.ModelViewSet):

    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer


class PostTagAPIView(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = PostTagSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeAPIView(generics.ListCreateAPIView):

    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
