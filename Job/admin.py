from django.contrib import admin
from Job.models import Post,Comment, Category, Time

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Time)

# Register your models here.
