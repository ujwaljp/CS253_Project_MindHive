from django.contrib import admin
from .models import Notification


# Register the notification model with the admin site
admin.site.register(Notification)