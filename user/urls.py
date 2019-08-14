from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.User_LogInView.as_view(), name='login'),
    path('logout/', views.User_LogOut.as_view(), name='logout'),
    path('followers/', views.User_followers.as_view(), name='user-follower'),
    path('following/', views.User_following.as_view(), name='user-following'),
    path('test/', views.Call_Index.as_view(), name='test'),

]