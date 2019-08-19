from django.urls import path

from api.job.views import Job_Create, Job_Update, Job_Delete, Job_likeView, Comment_Create, Reply_Create, Job_Like_View, \
    Job_Saved_View, Job_Notification_View, JobView_View

urlpatterns = [
    path('create/', Job_Create.as_view(), name='api-job-create'),
    path('comment/', Comment_Create.as_view(), name='api-comment-create'),
    path('reply/', Reply_Create.as_view(), name='api-reply-create'),
    path('update/<int:id>', Job_Update.as_view(), name='api-job-update'),
    path('delete/<int:id>', Job_Delete.as_view(), name='api-job-delete'),
    path('like/', Job_Like_View.as_view(), name='api-job-like'),
    path('save/', Job_Saved_View.as_view(), name='api-job-save'),
    path('notification/', Job_Notification_View.as_view(), name='api-job-notification'),
    path('view/', JobView_View.as_view(), name='api-job-view'),

    # path(),

]