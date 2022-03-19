from django.db import models

from datetime import datetime
from ckeditor.fields import RichTextField

class Content(models.Model):
    text = RichTextField()
    author = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, related_name='author', null=True)
    anonymous = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    likedBy = models.ManyToManyField(to='users.User', related_name='likedBy', blank=True)
    dislikedBy = models.ManyToManyField(to='users.User', related_name='dislikedBy', blank=True)

    def __str__(self):
        return self.text
    
    def show_description(self):
        return self.text[:70]
    
    def get_author_name(self):
        if self.anonymous:
            return 'Anonymous User'
        else:
            return self.author.name

    def get_author_id(self):
        if self.anonymous:
            return 'Anonymous User'
        else:
            return self.author_id