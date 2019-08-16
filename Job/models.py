from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    skills = models.TextField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, null=True, related_name='like_set')
    category = models.ForeignKey('Category',on_delete=models.DO_NOTHING, related_name='category', null=True)
    time = models.ForeignKey('Time', on_delete=models.DO_NOTHING, related_name='fulltime', null=True)



class Category(models.Model):
    categories = models.TextField(null=True)

    def __str__(self):
        return self.categories


class Time(models.Model):
    full_time = models.TextField(null=True)

    def __str__(self):
        return self.full_time


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')
    post = models.ForeignKey('Post', on_delete=models.DO_NOTHING)
    text = models.TextField(null=True)
    reply = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, related_name='replies', null=True)
    reply_is = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
# Create your models her