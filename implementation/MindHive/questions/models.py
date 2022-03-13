from django.db import models
from home.models import Content
class Question(Content):
    # Question-specific fields
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(to='tags.Tag',related_name='relatedto', blank=True)
    numViews = models.IntegerField(default=0)
    viewedBy = models.ManyToManyField(to='users.User', related_name='viewedBy', blank=True)