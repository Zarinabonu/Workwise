from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    skills = models.TextField(null=True)
    price = models.IntegerField()
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, null=True, related_name='like_set')


class Category(models.Model):
    post = models.ForeignKey('Post',on_delete=models.DO_NOTHING, related_name='category', null=True)
    categories = models.TextField(null=True)


class Time(models.Model):
    post = models.ForeignKey('Post', on_delete=models.DO_NOTHING, related_name='full_time', null=True)
    full_time = models.TextField(null=True)


class Comment(models.Model):
    project = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')
    text = models.TextField(null=True)
    reply = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, related_name='replies', null=True)

# Create your models her