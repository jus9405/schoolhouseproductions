from django.db import models
from django.contrib import admin
# Special import of the shows model.

from schoolhouseproductions.shows import Show

# Create your models here.

# Creating basic video model.

class Video(models.Model)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    publish_date = models.DateTimeField(auto_now_add=True)
    show = models.ForeignKey(Show)
    video_url = models.URLField(max_length=300)

admin.site.register(Video)
