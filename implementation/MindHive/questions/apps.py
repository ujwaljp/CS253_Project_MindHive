from django.apps import AppConfig


# Questions app config to register the app with Django
class QuestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questions'
