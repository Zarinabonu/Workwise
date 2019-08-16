from django.urls import path

from api.job.views import Job_Create, Job_Update, Job_Delete, Job_likeView, Comment_Create, Reply_Create

urlpatterns = [
    path('create/', Job_Create.as_view(), name='api-job-create'),
    path('comment/', Comment_Create.as_view(), name='api-comment-create'),
    path('reply/', Reply_Create.as_view(), name='api-reply-create'),
    path('update/<int:id>', Job_Update.as_view(), name='api-job-update'),
    path('delete/<int:id>', Job_Delete.as_view(), name='api-job-delete'),
    path('like/', Job_likeView.as_view(), name='api-job-like'),

]