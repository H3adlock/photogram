from django.urls import path
from .views import gallery, home, post, profile, edit_profile


urlpatterns = [
    path('', home, name="home"),
    path('gallery/', gallery, name="gallery"),
    path('post/<slug>', post, name="post-detail"),
    path('profile/', profile, name="account_profile"),
    path('profile/edit', edit_profile, name="edit_profile")

]
