from django.urls import path
from .views import MainPostList

urlpatterns = [
    path('posts/', MainPostList.as_view())
]
