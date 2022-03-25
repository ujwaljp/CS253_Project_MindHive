from django.test import TestCase
from answers.models import Answer

class AnswerModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
       Answer.objects.create(answer_text='test answer') 