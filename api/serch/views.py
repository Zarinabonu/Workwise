from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# from Project.models import Project


class Serach_View(APIView):
    def post(self,request):
        print(request.POST)
        # query_set = User.objects.filter(username__icontains=)
