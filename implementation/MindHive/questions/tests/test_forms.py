from django.test import TestCase
from questions.models import Question
from questions.forms import CreateQuestionForm
from users.models import User
from tags.models import Tag
from datetime import datetime


class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        Tag.objects.create(name="Anarchy")
        question = Question.objects.create(title='test',tags='Anarchy')

class QuestionFormTest(TestCase):
    def test_valid(self):
        tag=Tag.objects.create(name="Anarchy")
        form_data = {'title': 'user',
                     'text': 'Usertext',
                    #  'tags': "Anarchy",
                     'anonymous':False}
        form = CreateQuestionForm(data = form_data)
        self.assertFalse(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.title, "user")
        self.assertEqual(saved.text, "Usertext")
        # self.assertEqual(saved.tags, "Anarchy")
        self.assertEqual(saved.author, "user")
        self.assertEqual(saved.timestamp.date(),datetime.now().date())

class AnswerFormTest(TestCase):
    def test_valid(self):
        form_data = {'title': 'user',
                     'text': 'Usertext',
                    #  'tags': "Anarchy",
                     'anonymous':False}
        form = CreateQuestionForm(data = form_data)
        self.assertFalse(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.title, "user")
        self.assertEqual(saved.text, "Usertext")
        # self.assertEqual(saved.tags, "Anarchy")
        self.assertEqual(saved.author, "user")
        self.assertEqual(saved.timestamp.date(),datetime.now().date())

    