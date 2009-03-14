from django.db import models
from django.contrib import admin
# Create your models here.

class Show(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['name', 'creation_date', 'update_time']
        db_table = 'shows'
        get_latest_by = "update_time"

admin.site.register(Show)
