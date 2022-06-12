from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='homePage'),
    #path('api/awards/', views.ProfileList.as_view()),
    path('api/awards/', views.ProjectsList.as_view()),
    path('profile/<username>/', views.profile, name='profile'),
] 