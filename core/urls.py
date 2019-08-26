from django.urls import path
from .views import gallery, home, post


urlpatterns = [
    path('', home, name="home"),
    path('gallery/', gallery, name="gallery"),
    path('post/<slug>', post, name="post-detail")
]
