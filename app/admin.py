from __future__ import unicode_literals
from django.contrib import admin
from .models import Profile, Projects

# Register your models here.

admin.site.register(Projects)
admin.site.register(Profile)
