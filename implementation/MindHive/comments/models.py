from django.db import models
from home.models import Content
from questions.models import Question
from answers.models import Answer

# Create your models here.
class Comment(Content):
    parentObjType = models.CharField(max_length=200)
    parentObjQ = models.ForeignKey(Question, on_delete=models.CASCADE)
    parentObjA = models.ForeignKey(Answer, on_delete=models.CASCADE)