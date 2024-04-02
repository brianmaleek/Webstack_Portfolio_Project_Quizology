from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function that creates a profile for a newly created User instance.

    Args:
        sender: The sender of the signal.
        instance: The User instance that was saved.
        created: A boolean indicating whether the User instance was created or updated.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    A signal receiver function that is triggered after a User instance is saved.
    It saves the associated profile instance.

    Parameters:
        sender (class): The model class that sent the signal (User).
        instance (User): The actual instance being saved.
        kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    instance.profile.save()
