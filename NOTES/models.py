from django.db import models

# Create your models here.


class Books(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitles = models.CharField(max_length=200)
    pages = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
