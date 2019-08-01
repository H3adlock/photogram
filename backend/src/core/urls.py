from django.urls import path
from .views import gallery


app_name = 'core'

urlpatterns = [
    path('', gallery, name='gallery')
]
