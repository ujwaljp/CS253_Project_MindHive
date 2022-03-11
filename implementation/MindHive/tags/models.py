from django.db import models
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50)
    users_lst=models.ManyToManyField(to='users.User', related_name='favourite_of')

    def __str__(self):
        return self.name