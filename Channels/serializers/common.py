from rest_framework import serializers

# from reviews.serializers import PopulatedReviewSerializer
from ..models import *


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        # fields = ('id', 'title', 'image', 'release_date')
        fields = ('__all__')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('__all__')


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('__all__')
