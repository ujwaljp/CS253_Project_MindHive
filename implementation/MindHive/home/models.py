from django.db import models

class Content(models.Model):
    text = models.CharField(max_length=200)
    author = models.OneToOneField(to='users.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    numLikes = models.IntegerField(default=0)
    numDislikes = models.IntegerField(default=0)
    likedBy = models.ManyToManyField(to='users.User', related_name='likedBy', blank=True)
    dislikedBy = models.ManyToManyField(to='users.User', related_name='dislikedBy', blank=True)

    def __str__(self):
        return self.text