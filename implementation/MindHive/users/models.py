from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    blocked = models.BooleanField(default=False)
    followingQuestions = models.ManyToManyField(to='questions.Question', related_name='user_fq', blank=True)
    bookmarkQuestions = models.ManyToManyField(to='questions.Question', related_name='user_bq', blank=True)
    favouriteTags = models.ManyToManyField(to='tags.Tag', blank=True)
    notifications = models.ManyToManyField(to='notifications.Notification', blank=True)

    def __str__(self):
        return self.username

class Report(models.Model):
    report_text = models.CharField(max_length=200)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reportedUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported')
    reportedObjType = models.CharField(max_length=20)
    reportedObjQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, null=True, blank=True)
    reportedObjA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE, null=True, blank=True)
    reportedObjC = models.ForeignKey(to='comments.Comment', on_delete=models.CASCADE, null=True, blank=True)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_text