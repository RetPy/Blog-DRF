# Generated by Django 4.0.1 on 2022-01-18 14:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_remove_post_image_postimage_post_tag_postvideo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='liked_user',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post', 'user')},
        ),
    ]
