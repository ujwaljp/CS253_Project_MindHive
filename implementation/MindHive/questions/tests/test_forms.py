from django import forms, setup
from django.test import TestCase
from matplotlib import widgets
from questions.models import Question
from notifications.models import Notification
from questions.forms import CreateQuestionForm
from questions.forms import AddAnswerForm
from questions.forms import CreateReportForm
from users.models import User
from tags.models import Tag
from ckeditor.fields import RichTextField
from datetime import datetime
import pytz
class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        user1 = User(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        user1.save()
        tag = Tag.objects.create(name="Anarchy")
        # question = Question.objects.create(title='test',tags='Anarchy')

class QuestionFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        tag = Tag.objects.create(name="Anarchy")
        # forms.CheckboxSelectMultiple
        form_data = {'title': "user",
                     'text': "Usertext",
                     'tags': ['1'],
                     'author': user,
                     'anonymous':False}
        form = CreateQuestionForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.title, "user")
        self.assertEqual(saved.text, "Usertext")
        # self.assertEqual(saved.tags, tag)
        self.assertEqual(saved.author, user)

