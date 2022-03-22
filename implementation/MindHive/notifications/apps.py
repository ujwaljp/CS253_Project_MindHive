from django.apps import AppConfig


# NotificationsConfig class is used to register the notifications app with the admin site
class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'
