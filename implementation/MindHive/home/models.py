from email.policy import default
from django.db import models

from datetime import datetime
from ckeditor.fields import RichTextField


# content model, base class for the Question, Answer and Comment classes
class Content(models.Model):
    text = RichTextField(blank=False)
    author = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, related_name='author', null=True)
    anonymous = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', default = datetime.now(), blank=True, null=True)
    likedBy = models.ManyToManyField(to='users.User', related_name='likedBy', blank=True)
    dislikedBy = models.ManyToManyField(to='users.User', related_name='dislikedBy', blank=True)

    def __str__(self):
        """return the content's text with str(content) is called"""
        return self.text
    
    def show_description(self):
        """return the first 70 characters of the content's text"""
        return self.text[:70]
    
    def get_votes(self):
        """returns the total number of votes for a question"""
        return self.likedBy.count() - self.dislikedBy.count()
    
    def get_author_name(self):
        """return the author's name if anonymous is False, else return Anonymous User"""
        if self.anonymous:
            return 'Anonymous User'
        else:
            return self.author.username