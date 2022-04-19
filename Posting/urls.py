from django.urls import path
from .views import ChannelPostList, UserPostList

urlpatterns = [
    path('posts/', ChannelPostList.as_view()),
    # path('posts/', UserPostList.as_view())
]
