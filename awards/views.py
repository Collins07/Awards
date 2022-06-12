from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProjectsForm
from .models import Projects,Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer


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



# @login_required(login_url='/accounts/login/')
# def single_project(request, projects):
#     projects = Projects.objects.get(title=projects)


#     return render(request, 'single_project.html', {'project':projects})




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