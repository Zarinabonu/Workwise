from django.contrib import admin
from Project.models import Project, Category, Like, Comment

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
# Register your models here.
