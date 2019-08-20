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
    saved = models.ManyToManyField(User, null=True, related_name='save_set')
    category = models.ForeignKey('Category',on_delete=models.DO_NOTHING, related_name='category', null=True)
    time = models.ForeignKey('Time', on_delete=models.DO_NOTHING, related_name='fulltime', null=True)
    view = models.ManyToManyField(User, related_name='view_set')



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
    post = models.ForeignKey('Post', on_delete=models.DO_NOTHING, null=True)
    text = models.TextField(null=True, blank=True)
    reply = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, related_name='replies', null=True)
    reply_is = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receiver_notification')
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender_notification')
    post = models.ForeignKey('Post', on_delete=models.DO_NOTHING, related_name='post_notification')
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.text
# Create your models her