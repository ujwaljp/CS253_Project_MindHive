# from django import forms
# from django.test import TestCase
# from matplotlib import widgets
# from questions.models import Question
# from notifications.models import Notification
# from questions.forms import CreateQuestionForm
# from questions.forms import AddAnswerForm
# from questions.forms import CreateReportForm
# from users.models import User
# from tags.models import Tag
# from ckeditor.fields import RichTextField
# from datetime import datetime
# import pytz
# class Setup_Class(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
#         user1 = User(email="example@iitk.ac.in", username="eg", password="example",name="harish")
#         user1.save()
#         tag=Tag.objects.create(name="Anarchy")

# class QuestionFormTest(TestCase):
#     def test_valid(self):
#         t=RichTextField("So I have a question")
#         form_data = {'title': 'user',
#                     'author': 'self.user',
#                      'text': 't',
#                     'tags': ['1'],
#                      'anonymous':False}
#         form = CreateQuestionForm(data = form_data)
#         self.assertFalse(form.is_valid())
#         saved = form.save()
#         self.assertEqual(saved.title, "user")
#         self.assertEqual(saved.text, "Usertext")
#         # self.assertEqual(saved.tags, "Anarchy")
#         self.assertEqual(saved.author, "user")
#         self.assertEqual(saved.timestamp.date(),datetime.now().date())

# class AnswerFormTest(TestCase):
#     def test_valid(self):
#         form_data = {'title': 'user',
#                      'text': 'Usertext',
#                     #  'tags': "Anarchy",
#                      'anonymous':False}
#         form = CreateQuestionForm(data = form_data)
#         self.assertFalse(form.is_valid())
#         saved = form.save()
#         self.assertEqual(saved.title, "user")
#         self.assertEqual(saved.text, "Usertext")
#         # self.assertEqual(saved.tags, "Anarchy")
#         self.assertEqual(saved.author, "user")
#         self.assertEqual(saved.timestamp.date(),datetime.now().date())

    