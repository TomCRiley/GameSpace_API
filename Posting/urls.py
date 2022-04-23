from django.urls import path
from .views import UserCreatePost, UserPostList, UserPostUpdateDestroy

urlpatterns = [
    # view all posts on channel
    path('user/create/', UserCreatePost.as_view()),  # user create a post
    path('user/', UserPostList.as_view()),  # all posts by one user
    path('user/update/<int:pk>/',
         UserPostUpdateDestroy.as_view()),  # update/delete
]
