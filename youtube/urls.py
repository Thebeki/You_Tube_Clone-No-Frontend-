
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('thebeki/', admin.site.urls),
    path('', include('you_tube_rest.urls')),
]
