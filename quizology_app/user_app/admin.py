"""
This module is responsible for registering the Profile model in the Django admin site.

The Profile model represents user profiles in the application. By registering it with the admin site,
administrators can manage user profiles through the Django admin interface.

Usage:
    - Import the Profile model from the models module.
    - Register the Profile model with the admin site using the `admin.site.register()` function.
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
