from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from Channels.serializers.common import ChannelSerializer

from .models import *
from .serializers import *

# Create your views here.


class UserPostList(ListCreateAPIView):  # user profile page get all user posts
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        userid = self.request.query_params.get('user')
        if userid:
            queryset = queryset.filter(user_id=userid)
        return queryset


class ChannelPostList(ListCreateAPIView):  # all posts for one specific channel

    serializer_class = PostSerializer

    def get_queryset(self, request, pk):
        queryset = Post.objects.all()
        # channelid = self.request.query_params.get('channel')
        if pk:
            queryset = queryset.filter(channel_id=pk)
        return queryset


class UserCreatePost(ListCreateAPIView):  # user can create a post

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        request.data['first_name'] = request.user.id  # HELP what is this?

        main_post_serializer = PostSerializer(data=request.data)
        if main_post_serializer.is_valid():
            main_post_serializer.save()
            return Response(data=main_post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=main_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPostUpdateDestroy(APIView):

    permission_classes = [IsAuthenticated, ]

    def put(self, request, pk):
        post_to_update = self.get_post(pk=pk)

        if post_to_update.user.id != request.user.id:
            raise PermissionDenied

        request.data['channel'] = post_to_update.channel.id
        request.data['user'] = post_to_update.user.id
        post_update_serializer = PostSerializer(
            post_to_update, data=request.data)

        if post_update_serializer.is_valid():
            post_update_serializer.save()
            return Response(data=post_update_serializer.data, status=status.HTTP_200_OK)
        return Response(post_update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post_to_delete = self.get_post(pk=pk)

        if post_to_delete.user.id != request.user.id:
            raise PermissionDenied

        post_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound(detail="Post doesn't exit!")
