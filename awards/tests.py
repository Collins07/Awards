from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Collins', password='c0718074023')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class ProjectsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Collins')
        self.project = Projects.objects.create(id=1, title='this is an instagram clone project', photo='', description='',
                                        user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

    def test_save_projects(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_projects(self):
        self.project.save()
        projects = Projects.all_projects()
        self.assertTrue(len(projects) > 0)

    def test_search_project(self):
        self.project.save()
        project = Projects.search_project('')
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = Projects.search_project('')
        self.assertTrue(len(project) < 1)


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Collins')
        self.project = Projects.objects.create(id=1, title='this is an instagram clone project', photo='', description='',
                                        user=self.user)
        

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_project_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(project_id=id)
        self.assertTrue(len(rating) == 1)

