from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MainPostSerializer
# Create your views here.


class MainPostList(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        request.data['owner'] = request.user.id

        main_post_serializer = MainPostSerializer(data=request.data)
        if main_post_serializer.is_valid():
            main_post_serializer.save()
            return Response(data=main_post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=main_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
