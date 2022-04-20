from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import *
from .serializers.common import *


class ChannelList(ListCreateAPIView):  # lists all gamechannels across site
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

# detail view required?


class GameList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DeveloperList(ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
# user will be able to create new developers but not delete them


class PlatformList(ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
# user will not be able to delete platforms
