from django import template
from django.contrib.auth.models import User
from rest_framework import request

from Job.models import Notification

register = template.Library()

@register.simple_tag(name='not_list')
def noti_list(user):
    n = Notification.objects.filter(receiver=user)


    return n


@register.simple_tag(name='noti_list_read')
def noti_list_read(user):
    n = Notification.objects.filter(receiver=user)
    f = n.filter(read=False)

    return f