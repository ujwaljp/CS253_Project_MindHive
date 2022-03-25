from django.test import TestCase
from users.models import User
from tags.models import Tag
from answers.models import Answer
from ckeditor.fields import RichTextField
from datetime import datetime

class AnswerModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
       Answer.objects.create(answer_text='test answer') 