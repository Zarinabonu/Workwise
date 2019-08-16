from itertools import count

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import Job
from Job.models import Post, Category, Time, Comment
from Project.models import Project
import Project
from user.models import Profile


class User_LogInView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            print('Error')
        print(request.POST)
        print(user)
        return redirect(reverse('test'))


class User_LogOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('test'))


friend = 0


class Call_Index(View):
    def get(self, request):

        u = User.objects.get(username=request.user.username)
        f_set = u.profile.following.all()
        ids = f_set.values_list('id', flat=True)
        r = request.user.id
        ad = list(ids)
        ad.append(r)

        # lists = ad.append(r)
        # print(ad)
        # u = ids.append(request.user.id)
        # print('IDS ALL: ',ids, 'REQUEST :', r,' friends List :', ad,' ALL LISTS:'r)
        suggestions = User.objects.exclude(id__in=ids).filter(~Q(id=u.id)).annotate(count_suggest=Count('following')).order_by('-count_suggest')[:5]
        s_list = []
        for friend_my in f_set:
            for friend_f in friend_my.profile.following.all():
                if friend_f not in f_set:
                    if f_set.filter(profile__following__id=friend_f.id).count() >= 2:
                        if friend_f not in s_list:

                            s_list.append(friend_f)

        print(s_list)
        posts = Post.objects.all()
        categories = Category.objects.all()
        times = Time.objects.all()
        category_project = Project.models.Category.objects.all()
        posts = Post.objects.filter(pk__in=ad)

        # comment = Comment.objects.filtet(post__id=request.post.id)
        print('AA ', category_project)
        return render(request, 'index.html', {'suggestions': suggestions, 'suggest': s_list, 'categories': categories, 'time': times, 'category_pro': category_project,'posts':posts})


class User_followers(View):
    def get(self, request):
        u = request.user
        f = User.objects.get(id='1')
        f.profile.followers.add(u)

        f.save()


class User_following(APIView):
    def post(self, request):
        u = request.user
        print(request.user.username, ' ID  ', request.user.id)
        f = User.objects.get(id=request.POST.get('f_id'))
        print('User ', f)
        u.profile.following.add(f)

        # u = request.user
        # f = User.objects.get(id='1')
        f.profile.followers.add(u)

        f.save()

        return Response(status=status.HTTP_200_OK)

# Create your views here.
