from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser, models.Model):

    image = models.CharField(max_length=200)
    # posts = models.ForeignKey(
    #     MainPost, related_name='user', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
