from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Playlist)

