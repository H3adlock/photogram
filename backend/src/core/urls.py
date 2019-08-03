from django.urls import path
from .views import gallery, home, post


app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('post/', post, name='post')
]
