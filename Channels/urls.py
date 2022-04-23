from django.urls import path
from .views import *

urlpatterns = [
    # list all channels onserver
    path('channels/', ChannelList.as_view()),

    path('channel/<int:pk>/', SingleChannel.as_view()),

    # path('channel/<str:urlname>/', SingleChannelName.as_view()),
    # what it says on the tin
    path('channels/<int:pk>/', ChannelUpdateDestroy.as_view()),
    # path('channel details ') -- not sure if needed? --

    path('games/', GameList.as_view()),
    path('games/<int:pk>/', GameUpdateDestroy.as_view()),

    path('platforms/', PlatformList.as_view()),
    path('developers/', DeveloperList.as_view()),
]
