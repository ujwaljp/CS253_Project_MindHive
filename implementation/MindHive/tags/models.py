from django.db import models

# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    # __str__ method to return the name of the tag on calling str(tag)
    def __str__(self):
        return self.name