from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following')
    followers = models.ManyToManyField(User, related_name='followers')
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    job = models.TextField(null=True)


class Country(models.Model):
    name = models.CharField(max_length=100, null=True)

# Create your models here.
