from django.db import models
from home.models import Content

class Answer(Content):
    to_question = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE)