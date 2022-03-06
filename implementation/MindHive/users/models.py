from django.db import models
from ..questions.models import Question
from ..answers.models import Answer
from ..comments.models import Comment
from ..tags.models import Tag
from ..notifications.models import Notification

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    blocked = models.BooleanField(default=False)
    followingQuestions = models.ManyToManyField(Question, blank=True)
    bookmarkQuestions = models.ManyToManyField(Question, blank=True)
    favouriteTags = models.ManyToManyField(Tag, blank=True)
    notifications = models.ManyToManyField(Notification, blank=True)

    def __str__(self):
        return self.username

class Report(models.Model):
    report_text = models.CharField(max_length=200)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reportedUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported')
    reportedObjType = models.CharField(max_length=20)
    reportedObjQ = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    reportedObjA = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    reportedObjC = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_text