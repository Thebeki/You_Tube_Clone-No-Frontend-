
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *




urlpatterns = [

    path("videolist/", VideoListAPIView.as_view(), name='videolist'),
    path("playlist/", PlayListListAPIView.as_view(), name='playlist'),
    path("userlist/", UsersListAPIView.as_view(), name='userlist'),
    path("commentlist/", CommentListAPIView.as_view(), name='commentlist'),
]