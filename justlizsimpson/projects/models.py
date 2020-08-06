from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    github = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
