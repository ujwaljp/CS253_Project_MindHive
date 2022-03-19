from django.db import models

# Create your models here.
class Notification(models.Model):
    receivers = models.ManyToManyField(to='users.User', related_name='notifications', blank=True)
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    target_question = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
