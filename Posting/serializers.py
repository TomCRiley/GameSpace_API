from rest_framework import serializers
from .models import MainPost
from Users.serializers import UserSerializer


class MainPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPost
        fields = ('__all__')


class PopulatedMainPostSerializer(MainPostSerializer):

    owner = UserSerializer()
