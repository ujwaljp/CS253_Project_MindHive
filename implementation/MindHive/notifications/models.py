from django.db import models
from questions.models import Question
from answers.models import Answer

# Create your models here.
class Notification(models.Model):
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)
    contentType = models.CharField(max_length=20)
    contentQ = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    contentA = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text