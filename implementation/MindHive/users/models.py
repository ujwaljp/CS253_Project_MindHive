from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    blocked = models.BooleanField(default=False)
    followingQuestions = models.ManyToManyField('Question', blank=True)
    bookmarkQuestions = models.ManyToManyField('Question', blank=True)
    favouriteTags = models.ManyToManyField('Tag', blank=True)
    notifications = models.ManyToManyField('Notification', blank=True)

    def __str__(self):
        return self.username
