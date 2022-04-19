from django.urls import path
from .views import UserPostList

urlpatterns = [
    path('posts/', UserPostList.as_view())
]
