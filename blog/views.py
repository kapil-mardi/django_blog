from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):

    context = {
        'posts' : models.Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')
