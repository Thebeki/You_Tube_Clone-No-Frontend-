from django.db.models import fields
from rest_framework import serializers
from .import models
from rest_framework.exceptions import ValidationError

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Comment
        fields = ('id', 'description', 'video', 'userprofile')
class VideoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Video
        fields = ('id', 'name', 'userprofile' , 'video_location','viewers','creation_time_video', 'gender')


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.User
        fields = ('id', 'user', 'slug','profile_pic')

class PlaylistSerilaizer(serializers.ModelSerializer):
    class Meta: 
        model = models.Playlist
        fields = ('id', 'title', 'user','creation_time_playlist','video')
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ('id', 'user', 'slug','profile_pic')
