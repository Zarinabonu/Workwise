from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True)
    skills = models.TextField(null=True)
    price_from = models.IntegerField()
    price_to = models.IntegerField()
    description = models.TextField(null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING,related_name='categories_fields')
    likes = models.ManyToManyField(User, null=True, related_name='like_project')


class Category(models.Model):
    categories = models.CharField(max_length=50)

    def __str__(self):
        return self.categories


class Comment(models.Model):
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING, related_name='comment')
    text = models.TextField(null=True)
    parent = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, related_name='replies', null=True)

    def __str__(self):
        return self.project and self.parent





