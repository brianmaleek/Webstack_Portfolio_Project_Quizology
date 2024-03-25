# urls.py
from django.urls import path
# import views from the same directory
from . import views

# urlpatterns list routes URLs to views
urlpatterns = [
    path("", views.home, name="quiz_app-home"),
    path("about/", views.about, name="quiz_app-about"),
]
