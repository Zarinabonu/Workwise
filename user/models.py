from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from Job.models import Post
from Project.models import Project


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING, null=True, blank=True)
    job = models.TextField(null=True)
    save_job = models.ManyToManyField(Post, related_name='save_set')
    save_project = models.ManyToManyField(Project, related_name='save_set')


class Country(models.Model):
    name = models.CharField(max_length=100, null=True)


# class ChatRoom(models.Model):
#     user = models.ForeignKey(User, related_name='user_message', on_delete=models.DO_NOTHING)
#     name = models.TextField(null=True)
#     date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)