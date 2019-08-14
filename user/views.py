from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class User_LogInView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
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


class Call_Index(View):
    def get(self, request):
        return render(request, 'index.html')


class User_followers(View):
    def get(self, request):
        u = request.user
        f = User.objects.get(id='1')
        f.profile.followers.add(u)

        f.save()


class User_following(View):
    def get(self, request):
        u = request.user
        print(request.user.username,' ID  ',request.user.id)
        f = User.objects.get(id='1')
        print('User ',f)
        u.profile.following.add(f)


# Create your views here.
