from django.db import models
from home.models import Content

# Create your models here.
class Comment(Content):
    parentObjType = models.CharField(max_length=200)
    parentObjQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE)
    parentObjA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE)