from django.shortcuts import render
from .models import Image


def gallery(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'gallery.html')
