# programs/views.py
from rest_framework import generics
from .models import Program
from .serializers import ProgramSerializer
from .serializers import ProgramCreateSerializer


class ProgramListView(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramCreate(generics.CreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramCreateSerializer


class ProgramRetrieve(generics.RetrieveAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramUpdate(generics.UpdateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramDelete(generics.DestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
