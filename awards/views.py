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
    if request.method == "POST":
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
    else:
        form = ProjectsForm()

    return render(request, 'index.html', {'form': form})


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