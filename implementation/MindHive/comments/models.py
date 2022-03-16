from django.db import models
from home.models import Content

# Create your models here.
class Comment(Content):
    PARENT_OBJECT_TYPE = (
        ('q', 'Question'),
        ('a', 'Answer'),
    )
    parentObjType = models.CharField(max_length=1, choices=PARENT_OBJECT_TYPE)
    parentObjQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, blank=True, null=True)
    parentObjA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['pub_date']