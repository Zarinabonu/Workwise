
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user/', include('user.urls'))
    # path('user/', include('user.urls')),
    # path('project/', include('Project.urls')),
    # path('job/', include('Job.urls')),
]
if settings.DEBUG:
    urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
