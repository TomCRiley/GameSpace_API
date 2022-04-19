from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser, models.Model):

    username = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=150, null=True)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.username} ID:{self.id} "
