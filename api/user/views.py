from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from Job.models import Post
from Project.models import Project
from user.models import Profile
from .serializers import User_RegisterSerializer


class User_RegisterCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_RegisterSerializer


class Save_PostView(APIView):
    def get(self, request):
        p = Post.objects.get(id='1')
        print('VIEW ',p)
        re = request.user
        u = User.objects.get(id=request.user.id)
        u.profile.save_job.add(p)
        u.profile.save()
        return Response(status=status.HTTP_200_OK)


class Save_ProjectView(APIView):
    def get(self, request):
        p = Project.objects.get(id='1')
        u = User.objects.get(id=request.user.id)
        u.profile.save_project.add(p)
        u.profile.save()
        return Response(status=status.HTTP_200_OK)





