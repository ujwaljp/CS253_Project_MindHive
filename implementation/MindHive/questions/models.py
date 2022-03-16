from django.db import models
from django.urls import reverse

from home.models import Content

class Question(Content):
    # Question-specific fields
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(to='tags.Tag', blank=True)
    viewedBy = models.ManyToManyField(to='users.User', related_name='viewedBy', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('questions:view_question', kwargs={'pk': self.pk})