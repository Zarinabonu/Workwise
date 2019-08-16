from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import JobCreateSerializer, CommentSerializer, ReplySerializer
from Job.models import Post, Comment


class Job_Create(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = JobCreateSerializer


class Comment_Create(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Reply_Create(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ReplySerializer



class Job_Update(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = JobCreateSerializer
    lookup_url_kwarg = 'id'


class Job_Delete(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'id'

class Job_likeView(APIView):
    def get(self, request):
        print(request.GET)

        if request.GET.get('id'):

            p = Post.objects.get(id='1')
            u = request.user
            p.likes.add(u)
            p.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # u = request.user
        # print('USERNAME ', u)
        # return Response( status=status.HTTP_200_OK)
