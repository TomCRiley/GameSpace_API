from django.db import models
from Channels.models import Channel
from Users.models import CustomUser
# Create your models here.


class Post(models.Model):

    title = models.CharField(
        max_length=60, default="You should probably write a title....")
    # username = models.ForeignKey(
    #     CustomUser, related_name="posts", on_delete=models.CASCADE)
    createdDate = models.DateTimeField(null=True)
    text = models.CharField(max_length=500)
    channel_id = models.ForeignKey(
        Channel, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | posted by... {self.username}"


# class ChannelPosts(models.Model):
