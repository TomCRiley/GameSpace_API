from django.urls import path
from .views import *

urlpatterns = [
    path('channels/', ChannelList.as_view()),  # list all channels onserver
    # what it says on the tin
    path('channels/<int:pk>/', ChannelUpdateDestroy.as_view()),
    # path('channel details ') -- not sure if needed? --

    path('games/', GameList.as_view()),
    path('games/<int:pk>/', GameUpdateDestroy.as_view()),

    path('platforms/', PlatformList.as_view()),
    path('developers/', DeveloperList.as_view()),
]
