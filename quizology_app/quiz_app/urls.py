# urls.py
from django.urls import path
# import views from the same directory
from . import views

# urlpatterns list routes URLs to views
urlpatterns = [
    path("", views.home, name="quiz_app-home"),
    path("about/", views.about, name="quiz_app-about"),
    path("categories/", views.quiz_catergory_list, name="quiz_category_list"),
    path("quiz/<int:category_id>/", views.display_quiz, name="display_quiz"),
 ]
