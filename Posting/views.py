from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from .models import *
from .serializers import *

# Create your views here.


class UserPostList(ListCreateAPIView):  # endpoint for user profile page
    queryset = UserPost.objects.all()
    serializer_class = PostSerializer


# class AllChannelPosts(ListCreateAPIView):
#     queryset =


# class AllChannelPosts(APIView):

#     # permission_classes = [IsAuthenticated, ]

#     def get(self, request):
#         # request.data['owner'] = request.user.id

#         main_post_serializer = MainPostSerializer(data=request.data)
#         if main_post_serializer.is_valid():
#             main_post_serializer.save()
#             return Response(data=main_post_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=main_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
