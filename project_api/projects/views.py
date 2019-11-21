# projects/views.py
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from .serializers import ProjectCreateSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer


class ProjectRetrieve(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdate(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDelete(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
