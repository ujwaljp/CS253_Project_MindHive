from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractUser

# declare the userInfo model manager

class EmailValidator(RegexValidator):
    regex = '@iitk.ac.in$'
    message = 'Enter a valid email address'
    code = 'invalid_email'

class UserInfoManager(BaseUserManager):
    # function for creating a normal user
    def create_user(self, email, username, name, password,roll_no=None, ):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            roll_no=roll_no,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    # function for creating an admin user
    def create_superuser(self, email, username, password, name=None, roll_no=None):
        user = self.create_user(email=email, username=username, name=name,
                                roll_no=roll_no, password=password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

# declare the main User model by inheriting the AbstractUser model of Django
class User(AbstractUser):

    username = models.CharField(max_length=20,blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
        validators=[EmailValidator()]
    )

    name = models.CharField(max_length=20, blank=True, null=True)
    roll_no=models.CharField(max_length=8, blank=True, null=True)

    profile_image = models.ImageField(upload_to='profile_image', default='default.jpg')
    blocked = models.BooleanField(default=False)
    followingQuestions = models.ManyToManyField(to='questions.Question', related_name='users_following', blank=True)
    bookmarkQuestions = models.ManyToManyField(to='questions.Question', related_name='users_bookmarked', blank=True)
    favouriteTags = models.ManyToManyField(to='tags.Tag', blank=True)

    objects = UserInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' ]

    def __str__(self):
        return self.username

# model for reporting a question/user
class Report(models.Model):
    report_text = models.CharField(max_length=200)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reportedUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported')
    reported_on = models.DateTimeField(auto_now_add=True)
    REPORTED_OBJECT_TYPES = (
        ('q', 'Question'),
        ('a', 'Answer'),
        ('c', 'Comment'),
    )
    reportedObjType = models.CharField(max_length=1, choices=REPORTED_OBJECT_TYPES)
    reportedObjQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, null=True, blank=True)
    reportedObjA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE, null=True, blank=True)
    reportedObjC = models.ForeignKey(to='comments.Comment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.report_text
