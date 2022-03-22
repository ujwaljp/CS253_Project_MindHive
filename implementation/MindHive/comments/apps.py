from django.apps import AppConfig


# CommentsConfig class to register the comments app with Django.
class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
