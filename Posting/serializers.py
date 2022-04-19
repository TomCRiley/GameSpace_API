from rest_framework import serializers
from .models import UserPost
from Users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPost
        fields = ('__all__')


class PopulatedUserPostSerializer(PostSerializer):

    owner = UserSerializer()
