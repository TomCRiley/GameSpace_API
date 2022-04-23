from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import *
from .serializers.common import *


# lists all gamechannels, create new game channels across site
class ChannelList(ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class SingleChannel(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


# class SingleChannelName(RetrieveAPIView):
#     serializer_class = ChannelSerializer

#     def get_queryset(self, request, urlName):
#         queryset = Channel.objects.all()
#         # urlName = self.request.query_params.get()
#         if urlName:
#             queryset = queryset.filter(urlName=urlName)
#         return queryset


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
