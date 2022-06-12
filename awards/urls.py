from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.index, name='homePage'),
    path('api/awards/profiles/', views.ProfileList.as_view()),
    path('api/awards/projects/', views.ProjectsList.as_view()),
    path('profile/<username>/', views.profile, name='profile'),
    #path('project/<projects>', views.single_project, name='project'),
    path('search/', views.search_project, name='search'),
    path('profile/<username>/update', views.edit_profile, name='update'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('project/<id>', views.project, name='project'),

] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
