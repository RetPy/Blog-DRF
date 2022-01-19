from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Tag(models.Model):

    text = models.CharField(
        max_length=255,
        db_index=True,
        unique=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )

    def __str__(self):
        return self.text


class Post(models.Model):

    title = models.CharField(
        max_length=255
    )
    text = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_post'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='tag_post'
    )

    def __str__(self):
        return self.title


class PostImage(models.Model):

    image = models.ImageField(
        upload_to='post_images',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_image'
    )

    def __str__(self):
        return self.post.title


class Like(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='like_post'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like_user'
    )

    class Meta:

        unique_together = ('post', 'user')

    def __str__(self):
        return self.post.title


class PostVideo(models.Model):

    video = models.FileField(
        upload_to='video'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_video'
    )

    def __str__(self):
        return self.post.title
