from django.db import models


# Notification model
class Notification(models.Model):
    receivers = models.ManyToManyField(
        to='users.User', related_name='notifications', blank=True)
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    target_question = models.ForeignKey(
        to='questions.Question', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        ordering = ['-timestamp',]

    def __str__(self):
        """return the text of the notification on str(notification) call"""
        return self.text
