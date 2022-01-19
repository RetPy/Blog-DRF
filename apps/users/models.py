from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    age = models.PositiveIntegerField(
        default=0
    )
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICE
    )

    def __str__(self):
        return self.username
    