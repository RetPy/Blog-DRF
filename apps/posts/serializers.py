from rest_framework import serializers

from apps.posts.models import *
from apps.comments.serializers import CommentSerializer


class PostLikeSerializer(serializers.ModelSerializer):

    user = serializers.CharField(read_only=True)

    class Meta:

        model = Like
        fields = '__all__'


class PostTagSerializer(serializers.ModelSerializer):

    user = serializers.CharField(read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class PostVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostVideo
        fields = '__all__'


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = PostImage
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    total_likes = serializers.SerializerMethodField()
    post_video = PostVideoSerializer(read_only=True, many=True)
    post_image = PostImageSerializer(read_only=True, many=True)
    comment_post = CommentSerializer(read_only=True, many=True)
    user = serializers.CharField(read_only=True)

    class Meta:

        model = Post
        fields = '__all__'

    def get_total_likes(self, instance):
        return instance.like_post.all().count()


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
