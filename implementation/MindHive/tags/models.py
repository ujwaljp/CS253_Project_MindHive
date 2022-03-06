from django.db import models
from django.forms import CharField
from ..users.models import User
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50)
    users_lst=models.ManyToManyField(User, related_name='favourite_of')
