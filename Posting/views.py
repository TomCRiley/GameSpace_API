from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.


class UserPostList(ListCreateAPIView):  # user profile page get all user posts
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        userid = self.request.query_params.get('id')
        if userid:
            queryset = queryset.filter(user_id=userid)
        return queryset


class ChannelPostList(ListCreateAPIView):  # all posts for one specific channel
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        channelid = self.request.query_params.get('id')
        if channelid:
            queryset = queryset.filter(channel_id=channelid)
        return queryset


class UserCreatePost(ListCreateAPIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        request.data['first_name'] = request.user.id  # HELP what is this?

        main_post_serializer = PostSerializer(data=request.data)
        if main_post_serializer.is_valid():
            main_post_serializer.save()
            return Response(data=main_post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=main_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
