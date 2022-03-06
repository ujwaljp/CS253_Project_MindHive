from django.db import models

# Create your models here.
class Notification(models.Model):
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.text