from django.urls import path
from .views import ChannelPostList, UserPostList, UserPostUpdateDestroy

urlpatterns = [
    path('channel/posts/', ChannelPostList.as_view()),
    path('user/posts/', UserPostList.as_view()),
    path('user/posts/update/<int:pk>/', UserPostUpdateDestroy.as_view()),
]
