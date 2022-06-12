from .models import Profile, Projects
from django import forms

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'image','description', 'url'] 