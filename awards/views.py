from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectsForm,UserForm,ProfileForm,RatingsForm
from .models import Projects,Profile,Rating
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
@login_required (login_url='/accounts/login/')
def index(request):
    current_user = request.user
    if request.method == "POST":
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
    else:
        form = ProjectsForm()
        projects = Projects.objects.all()

    return render(request, 'index.html', {'form':form, 'projects':projects})





@login_required(login_url='/accounts/login/')
def profile(request, username):
    projects = request.user.projects.all()

    return render(request, 'profile.html', {'projects':projects})





@login_required(login_url='/accounts/login/')
def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Projects.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'

        return render(request, 'results.html', {'results':results, 'message': message})
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})




@login_required(login_url='/accounts/login/')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'prof_form': prof_form})    



@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)

    return render(request, 'userprofile.html', {'user_prof': user_prof})



@login_required(login_url='/accounts/login/')
def project(request, id):
    project = get_object_or_404(Projects, pk=id)
    current_user = request.user
    # if request.method == 'POST':
    #     form = RatingsForm(request.POST)
    #     if form.is_valid():
    #         rate = form.save(commit=False)
    #         rate.user = current_user
    #         rate.save()

    form = RatingsForm()


    return render(request, 'single_project.html', {'project': project, 'form': form})




class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)

        return Response(serializers.data)


class ProjectsList(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)

        return Response(serializers.data)    