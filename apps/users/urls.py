from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.users.views import *
from apps.posts.views import *
from apps.comments.views import *

router = DefaultRouter()
router.register(
    'user',
    UserAPIView,
    basename='users'
)
router.register(
    'post',
    PostAPIView,
    basename='post-api'
)
router.register(
    'image',
    PostImageAPIView,
    basename='post-image'
)
router.register(
    'video',
    PostVideoAPIView,
    basename='post-video'
)
router.register(
    'tag',
    PostTagAPIView,
    basename='tags'
)
router.register(
    'comment',
    CommentAPIView,
    basename='comments'
)

urlpatterns = [
    path('like/', PostLikeAPIView.as_view(), name='like')
]

urlpatterns += router.urls
