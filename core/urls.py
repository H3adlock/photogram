from django.urls import path
from .views import gallery, home, post, profile


urlpatterns = [
    path('', home, name="home"),
    path('gallery/', gallery, name="gallery"),
    path('post/<slug>', post, name="post-detail"),
    path('profile/', profile, name="account_profile")
]
