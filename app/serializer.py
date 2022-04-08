from rest_framework import serializers
from .models import Profile, Project


# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "profile_photo", "bio", "contact")


# Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("user", "title", "description", "image", "url", "location", "date")