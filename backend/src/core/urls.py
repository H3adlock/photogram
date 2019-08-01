from django.urls import path
from .views import gallery


app_name = 'core'

urlpattern = [
    path('', gallery, name='gallery')
]
