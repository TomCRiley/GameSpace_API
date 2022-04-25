from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import *
from .serializers.common import *
from rest_framework.response import Response


# lists all gamechannels, create new game channels across site
class ChannelList(ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class SingleChannel(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


# class UrlNameChannel(RetrieveAPIView):
#     def get(self, request, urlname):
#         channels = list(Channel.objects.filter(urlname=urlname))
#         if len(channels) == 0:
#             Response(status=404)
#         channel_serializer = ChannelSerializer(channels[0])
#         return Response(data=channel_serializer.data)

class UrlNameChannel(RetrieveAPIView):

    def get(self, request, urlname):

        queryset = Channel.objects.filter(urlname=urlname)
        if (queryset.len() == 0):
            Response(status=404)

        channels = list(queryset)
        channel_serializer = ChannelSerializer(channels[0])
        return Response(data=channel_serializer.data)


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
