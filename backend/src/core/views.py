from django.shortcuts import render
from .models import Post


def home(request):
    featured = Post.objects.filter(featured=True)[0:5]
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
    }
    return render(request, 'index.html', context)


def post(request):
    return render(request, 'post.html', {})


def gallery(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'gallery.html', context)
