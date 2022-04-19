from django.db import models
from Users.models import CustomUser
# Create your models here.


class Post(models.Model):  # rename to just Posts

    title = models.CharField(
        max_length=60, default="You should probably write a title....")
    username = models.ForeignKey(
        CustomUser, related_name="posts", on_delete=models.PROTECT)
    createdDate = models.DateTimeField(null=True)
    # channel ID

    def __str__(self):
        return f"{self.title} written by {self.username} is: {self.text} written at {self.created_date}"

# class ChannelPosts(models.Model):
