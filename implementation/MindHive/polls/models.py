from django.db import models
from home.models import Content

class Question_for_polls(Content):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(to='tags.Tag', blank=True)
    viewedBy = models.ManyToManyField(to='users.User', related_name='polls_viewedBy', blank=True)


class Choice(models.Model):
    question = models.ForeignKey(Question_for_polls, on_delete=models.CASCADE,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)