from django.db import models
import datetime as dt

# cloudinary
from django.contrib.auth.models import User


# project models
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Nairobi")
    # usability_rate = models.IntegerField(default=0, blank=True, null=True)
    # content_rate = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)