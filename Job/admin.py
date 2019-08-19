from django.contrib import admin
from Job.models import Post,Comment, Category, Time, Notification

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Time)
admin.site.register(Notification)

# Register your models here.
