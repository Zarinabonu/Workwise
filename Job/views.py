from django.shortcuts import render
from django.views.generic import ListView
from Job.models import Post


class Category_ListView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'job_posts'

# Create your views here.
