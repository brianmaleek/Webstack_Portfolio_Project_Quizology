"""
URL configuration for quizology_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('quizology_app/', include('quiz_app.urls'))
"""

# Import necessary modules
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user_app import views as user_views
from django.conf import settings
from django.conf.urls.static import static

def create_urlpatterns():
    """
    Creates URL patterns for the Django project.

    Returns:
        list: List of URL patterns.
    """

    urlpatterns = [
        # Admin site URL pattern
        path('admin/', admin.site.urls),

        # User registration URL pattern
        path('register/', user_views.register, name='register'),

        # User login URL pattern using Django's built-in authentication view
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

        # User logout URL pattern using Django's built-in authentication view
        # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
        path('logout/', user_views.logout_view, name='logout'),

        # User profile URL pattern
        path('profile/', user_views.profile, name='profile'),

        # Include URLs from the quiz app
        path('', include('quiz_app.urls')),  # Empty string matches the root URL
    ]
    
    return urlpatterns

urlpatterns = create_urlpatterns()

# Add URL patterns for media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
