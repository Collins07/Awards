from .models import Profile, Projects
from django import forms
from django.contrib.auth.models import User


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'image','description', 'url'] 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=300, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')         