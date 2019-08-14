from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import Project_CreateSerializer
from Project.models import Project


class Project_Create(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_CreateSerializer