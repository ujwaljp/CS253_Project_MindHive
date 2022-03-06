from tkinter import CASCADE
from django.db import models
from ..MindHive.models import Content

# Create your models here.
class Comment(Content):
    parentObjType : models.CharField(max_length=200)
    parentObj : models.ForeignKey(Content, on_delete=CASCADE)