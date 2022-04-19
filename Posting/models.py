from django.db import models
from Users.models import CustomUser
# Create your models here.


class MainPost(models.Model):

    title = models.CharField(max_length=60, default="default_title")
    username = models.ForeignKey(
        CustomUser, related_name="posts", on_delete=models.PROTECT)
    createdDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
