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

class QuestionFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
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

class AnswerFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        tag = Tag.objects.create(name="Anarchy")
        question = Question.objects.create(title='test',author=user)
        question.tags.set([tag])
        form_data = {'text': 'Usertext',
                     'author': user,
                     'anonymous':False,
                     'to_question': question}
                     
        form = AddAnswerForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.text, "Usertext")
        # self.assertEqual(saved.tags, "Anarchy")
        # self.assertEqual(saved.author, user)
        # self.assertEqual(saved.timestamp.date(),datetime.now().date())

class ReportFormTest(TestCase):
    def test_valid(self):
        user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
        user1 = User.objects.create(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        tag = Tag.objects.create(name="Anarchy")
        question = Question.objects.create(title='test',author=user)
        question.tags.set([tag])
        # answer = Answer.objects.create(text='Usertext',author=user,to_question=question)
        # comment = Comment.objects.create(text='Usertext',author=user)
        form_data = {'report_text': 'Usertext',
                     'reporter': user,
                     'reported_user': user1,
                     'reportedObjType': 'q',
                     'reportedObjQ': question,
                     'reportedObjA': None,
                     'reportedObjC': None}
        form = CreateReportForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.report_text, "Usertext")
