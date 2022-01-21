from django.db.models import fields
from rest_framework import serializers
from .import models
from rest_framework.exceptions import ValidationError

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Comment
        fields = '__all__'
class VideoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Video
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.User
        fields = '__all__'

class PlaylistSerilaizer(serializers.ModelSerializer):
    class Meta: 
        model = models.Playlist
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
