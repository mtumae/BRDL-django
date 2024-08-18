from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("blog", views.blog, name="blog"),
    path("add-blog", views.makepost, name="makepost"),
    path("contact", views.contact, name="contact"),
    path("lifestyle", views.lifestyle, name="lifestyle"),
    path("location", views.location, name="location"),
    path("gallery", views.gallery, name="gallery"),
    path("legacy", views.legacy, name="legacy")
]