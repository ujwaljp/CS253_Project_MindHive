import re

from django.db import models
from home.models import Content


# Comment model inherits from Content model and adds some fields for parent object
class Comment(Content):
    PARENT_OBJECT_TYPE = (
        ('q', 'Question'),
        ('a', 'Answer'),
    )
    parentObjType = models.CharField(max_length=1, choices=PARENT_OBJECT_TYPE)
    parentObjQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, blank=True, null=True)
    parentObjA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE, blank=True, null=True)

    # the meta class is used for ordering the comments based on the pub_date
    class Meta:
        ordering = ['pub_date']
    
    def get_text(self):
        """returns the text of the comment after removing html tags"""
        return re.sub(r'<[^>]*?>', '', self.text)