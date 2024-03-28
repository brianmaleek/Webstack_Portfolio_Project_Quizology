from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_app'

# 
    def ready(self):
        """
        This method is called when the application is ready to handle requests.
        It imports the signals module from the user_app package.
        """
        import user_app.signals
