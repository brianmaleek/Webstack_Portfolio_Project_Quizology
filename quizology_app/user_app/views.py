'''
Description: This file contains the views for the user app.
'''

# import render from django.shortcuts
from django.shortcuts import render, redirect

# import django messages to display one-time notifications.
from django.contrib import messages

# import forms from user_app
from .forms import UserRegisterForm

# login required for profile view
# from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    """
    View function for user registration.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the registration form.

    """
    if request.method == 'POST':
        # create instance of form with data from the request
        form = UserRegisterForm(request.POST)
        # check if form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect ('login')
    else:
        # create instance of form
        form = UserRegisterForm()

    # render the registration form, passing the form instance
    return render(request, 'register.html', {'form': form})


def logout(request):
    """
    View function for user logout.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the logout form.

    """
    logout(request)
    return render(request, 'logout.html')


""" @login_required
def profile(request):
    return render(request, 'user_app/profile.html') """
