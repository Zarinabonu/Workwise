from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('job/', include('api.job.urls')),
    path('project/', include('api.project.urls')),

]
