from django.urls import path
from .views import ChannelPostList

urlpatterns = [
    path('posts/', ChannelPostList.as_view())
]
