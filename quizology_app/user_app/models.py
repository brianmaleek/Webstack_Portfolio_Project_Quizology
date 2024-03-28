"""
This module contains the Profile model.
"""
# import models from django
from django.db import models
# import User model from django.contrib.auth.models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A model representing a user profile.

    Attributes:
        user (User): The user associated with the profile.
        image (ImageField): The profile picture of the user.

    Methods:
        __str__(): Returns a string representation of the profile.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
