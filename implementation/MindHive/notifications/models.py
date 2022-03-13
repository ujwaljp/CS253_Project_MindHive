from django.db import models

# Create your models here.
class Notification(models.Model):
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)
    CONTENT_TYPE = (
        ('q', 'Question'),
        ('a', 'Answer')
    )
    contentType = models.CharField(max_length=20)
    contentQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, null=True, blank=True)
    contentA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text