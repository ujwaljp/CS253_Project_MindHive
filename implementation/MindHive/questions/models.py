import re

from django.db import models
from django.urls import reverse

from home.models import Content


# Question class/model inherits from Content class
class Question(Content):
    # Question-specific fields
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(to='tags.Tag', blank=False)
    viewedBy = models.ManyToManyField(to='users.User', related_name='viewedBy', blank=True)

    def __str__(self):
        """returns the title of the question"""
        return self.title
    
    def get_absolute_url(self):
        """returns the url to access a particular question instance"""
        return reverse('questions:view_question', args=[self.pk])

    def get_summary_text(self):
        """returns the summary text of the question after removing html tags"""
        text = re.sub(r'<.*?>|&+.*;+', '', self.text)
        return text[:100] + '...'


    # order the questions based on publication date
    class Meta:
        ordering = ['-pub_date']