from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=120)
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

    @property
    def averages(self):
        return Rating.objects.filter(projects=self).aggregate(models.Avg('usability'), models.Avg('design'), models.Avg('content'))    

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



class Rating(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ratings', null=True)
    design = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    content = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(10)])

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(projects_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.projects} Rating'        