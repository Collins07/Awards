from django.db.models import fields
from rest_framework import serializers
from .models import Projects,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'profile_picture', 'bio', 'contact')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'image','description', 'url') 