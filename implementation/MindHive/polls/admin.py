from django.contrib import admin
from .models import Question_for_polls,Choice


# Register the notification model with the admin site
admin.site.register(Question_for_polls)
admin.site.register(Choice)
