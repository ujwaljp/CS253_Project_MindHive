from django.db import models
from home.models import Content
from questions.models import Question

class Answer(Content):
    parentObj=models.ForeignKey(Question, on_delete=models.CASCADE)