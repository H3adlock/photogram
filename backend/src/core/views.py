from django.shortcuts import render
from .models import Image


def home(request):
    return render(request, 'index.html', {})


def post(request):
    return render(request, 'post.html', {})


def gallery(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'gallery.html', context)
