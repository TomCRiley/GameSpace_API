from django.urls import path
from .views import ChannelPostList, UserCreatePost, UserPostList, UserPostUpdateDestroy

urlpatterns = [
    # view all posts on channel
    path('channel/', ChannelPostList.as_view()),
    path('user/create/', UserCreatePost.as_view()),  # user create a post
    path('user/', UserPostList.as_view()),  # all posts by one user
    path('user/update/<int:pk>/',
         UserPostUpdateDestroy.as_view()),  # update/delete
]
