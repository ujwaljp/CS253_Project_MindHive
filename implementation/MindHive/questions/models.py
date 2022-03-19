import re

from django.db import models
from django.urls import reverse

from home.models import Content

class Question(Content):
    # Question-specific fields
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(to='tags.Tag', blank=True)
    viewedBy = models.ManyToManyField(to='users.User', related_name='viewedBy', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('questions:view_question', args=[self.pk])
    
    def get_votes(self):
        return self.likedBy.count() - self.dislikedBy.count()

    def get_summary_text(self):
        # remove html tags
        text = re.sub(r'<.*?>|&+.*;+', '', self.text)
        return text[:100] + '...'

    class Meta:
        ordering = ['-pub_date']