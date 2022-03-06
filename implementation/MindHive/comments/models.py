from tkinter import CASCADE
from django.db import models
from ..MindHive.models import Content
from ..questions.models import Question
from ..answers.models import Answer

# Create your models here.
class Comment(Content):
    parentObjType = models.CharField(max_length=200)
    parentObjQ = models.ForeignKey(Question, on_delete=CASCADE)
    parentObjA = models.ForeignKey(Answer, on_delete=CASCADE)