from django.db import models
from home.models import Content

class Answer(Content):
    parentObj=models.ForeignKey(to='questions.Question', on_delete=models.CASCADE)