from rest_framework import serializers
from .models import Post
from Users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'username', 'createdDate', 'text']


class PopulatedPostSerializer(PostSerializer):

    owner = UserSerializer()
