import json

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# from Project.models import Project


class Serach_View(View):
    def get(self,request):
        print(request.GET)
        ulist = User.objects.filter(username__icontains=request.GET.get('term'))
        print(ulist)
        results = []
        for r in ulist:
            results.append(r.username)
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
        # query_set = User.objects.filter(username__icontains=)
