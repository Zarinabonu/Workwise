from itertools import count

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# import Job
from Job.models import Post, Category, Time, Comment, Notification
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

        suggestions = User.objects.exclude(id__in=ids).filter(~Q(id=u.id)).annotate(count_suggest=Count('following')).order_by('-count_suggest')[:5]
        s_list = []
        for friend_my in f_set:
            for friend_f in friend_my.profile.following.all():
                if friend_f not in f_set:
                    if f_set.filter(profile__following__id=friend_f.id).count() >= 2:
                        if friend_f not in s_list:

                            s_list.append(friend_f)

        # print(s_list)
        posts = Post.objects.all()
        categories = Category.objects.all()
        times = Time.objects.all()
        category_project = Project.models.Category.objects.all()
        posts = Post.objects.filter(pk__in=ad)
        top = Post.objects.all().order_by('-price')[:5]
        viewed = Post.objects.all().order_by('-view')[:3]
        n = Notification.objects.filter(receiver=request.user)

        # print('JOB TOP :',top)

        # comment = Comment.objects.filtet(post__id=request.post.id)
        # print('AA ', category_project)
        return render(request, 'index.html', {'suggestions': suggestions,
                                              'suggest': s_list,
                                              'categories': categories,
                                              'time': times,
                                              'category_pro': category_project,
                                              'posts': posts,
                                              'top_set': top,
                                              'm_viewed': viewed,
                                              'notifications': n})


class User_followers(View):
    def get(self, request):
        u = request.user
        f = User.objects.get(id='1')
        f.profile.followers.add(u)

        f.save()


class User_following(APIView):
    def post(self, request):
        u = request.user
        # print(request.user.username, ' ID  ', request.user.id)
        f = User.objects.get(id=request.POST.get('f_id'))
        # print('User ', f)
        u.profile.following.add(f)

        # u = request.user
        # f = User.objects.get(id='1')
        f.profile.followers.add(u)

        f.save()

        return Response(status=status.HTTP_200_OK)


class Person_DetailView(DetailView):
    template_name = 'profile/detail.html'
    model = User
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super(Person_DetailView, self).get_context_data(**kwargs)
        user_id = self.kwargs['pk']

        p = User.objects.get(id=user_id)
        context['f_set'] = p.profile.following.all()
        ids = context['f_set'].values_list('id', flat=True)
        ad = list(ids)
        context['s_list'] = []

        for friend_my in context['f_set']:
            for friend_f in friend_my.profile.following.all():
                if friend_f not in context['f_set']:
                    if context['f_set'].filter(profile__following__id=friend_f.id).count() >= 2:
                        if friend_f not in context['s_list']:
                            context['s_list'].append(friend_f)

        # posts = Post.objects.all()
        context['categories'] = Category.objects.all()
        context['times'] = Time.objects.all()
        context['category_project'] = Project.models.Category.objects.all()
        context['posts'] = Post.objects.filter(pk__in=ad)
        context['top'] = Post.objects.all().order_by('-price')[:5]
        context['viewed'] = Post.objects.all().order_by('-view')[:3]

        ctx = {'user': p,
            'category': context['categories'],
            'suggest': context['s_list'],
            'time': context['times'],
            'category_pro': context['category_project'],
            'posts': context['posts'],
            'top_set': context['top'],
            'm_viewed': context['viewed']

        }


        return ctx


class Person_detail_byUsername(View):
    def post(self, request):
        u = request.POST.get('username')
        p = User.objects.get(username=u)
        return HttpResponse(p.id)






