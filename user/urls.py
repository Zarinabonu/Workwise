from django.urls import path

from api.serch.views import Serach_View
from user import views

urlpatterns = [
    path('login/', views.User_LogInView.as_view(), name='login'),
    path('logout/', views.User_LogOut.as_view(), name='logout'),
    path('followers/', views.User_followers.as_view(), name='user-follower'),
    path('following/', views.User_following.as_view(), name='user-following'),
    path('test/', views.Call_Index.as_view(), name='test'),
    path('detail/<int:pk>', views.Person_DetailView.as_view(), name='user-detail'),
    path('search/', Serach_View.as_view(), name='user-search'),

]