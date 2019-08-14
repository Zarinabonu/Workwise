from django.urls import path

from api.user.views import User_RegisterCreate, Save_PostView, Save_ProjectView

urlpatterns = [
    path('create/', User_RegisterCreate.as_view(), name='api-register-create'),
    path('view/', Save_PostView.as_view(), name='api-view'),
    path('project/', Save_ProjectView.as_view(), name='api-project'),

]
