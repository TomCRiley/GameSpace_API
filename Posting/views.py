from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.


# all posts -  needs channel ID filter to be channel specific
class ChannelPostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserCreatePost(ListCreateAPIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        request.data['username'] = request.user.id

        main_post_serializer = PostSerializer(data=request.data)
        if main_post_serializer.is_valid():
            main_post_serializer.save()
            return Response(data=main_post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=main_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
