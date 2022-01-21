from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import FileExtensionValidator
# Create your models here.

class Video(models.Model):
    nom = models.CharField(max_length=255)
    video_joylashuvi = models.URLField()
    tomoshalar = models.IntegerField()
    video_yaratilgan = models.DateField(auto_now_add=False)
    JINS_CHOICES = (
        ('P', 'popular'),
        ('U', 'unpopular'),
    )
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    jins = models.CharField(max_length=1, choices=JINS_CHOICES)
    def __str__(self):
        return self.name
class Playlist(models.Model):
    sarlavha = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_yaratilgan = models.DateField(auto_now_add=True)
    video = models.ManyToManyField(Video, blank=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    video = models.ForeignKey(Video, blank=True, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.video.name

class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="userprofile")
    slug = models.SlugField(max_length=2000,unique=True,blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile/images/',validators=[FileExtensionValidator( ['png','jpg'] )],blank=True,null=True)
    def __str__(self):
        return self.user


