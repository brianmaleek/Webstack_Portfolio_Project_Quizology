'''
Description: This file contains the views for the user app.
'''

# import render from django.shortcuts
from django.shortcuts import render

# import user creation form from authentication module
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """
    View function for user registration.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the registration form.

    """
    # create instance of form
    form = UserCreationForm()
    # render the registration form, passing the form instance
    return render(request, 'register.html', {'form': form})
