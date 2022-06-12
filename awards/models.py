from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image',null=True, default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'




class Projects(models.Model):
    title = models.CharField(max_length=300)
    image = CloudinaryField('image',null=True)
    description = models.TextField()
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    date = models.DateTimeField(auto_now_add=True, blank=True)    

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.title}'    