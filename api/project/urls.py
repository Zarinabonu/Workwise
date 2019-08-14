from django.urls import path

from api.project.views import Project_Create

urlpatterns = [
    path('create/', Project_Create.as_view(), name='api-project-create'),
]