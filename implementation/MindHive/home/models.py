from django.db import models
from users.models import User

class Content(models.Model):
    text = models.CharField(max_length=200)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    numLikes = models.IntegerField(default=0)
    numDislikes = models.IntegerField(default=0)
    likedBy = models.ManyToManyField(User, related_name='likedBy')
    dislikedBy = models.ManyToManyField(User, related_name='dislikedBy')

    def __str__(self):
        return self.text