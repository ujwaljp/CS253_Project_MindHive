from django.test import TestCase
from users.models import User
from tags.models import Tag
from answers.models import Answer
from ckeditor.fields import RichTextField
from datetime import datetime
from questions.models import Question
import pytz
class AnswerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        text_content=RichTextField("So I have a question")
        user1 = User(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        user3 = User(email="example3@iitk.ac.in", username="eg3", password="example3",name="harish3")
        user2 = User(email="example2@iitk.ac.in", username="eg2", password="example2",name="harish2")
        user1.save()
        user3.save()
        user2.save()
        tag=Tag.objects.create(name="tag1")
        question1=Question.objects.create(text=text_content, author=user1, anonymous=False, pub_date=datetime(2020,1,1,0,0,0,tzinfo=pytz.UTC),title="How to do this?")
        question1.likedBy.add(user1)
        question1.tags.add(tag)
        question1.save()
        answer1=Answer.objects.create(text=RichTextField("Why dont you try using bertands theorem"), author=user2, anonymous=False, pub_date=datetime(2020,1,1,1,1,1,tzinfo=pytz.UTC),to_question=question1)
        answer1.likedBy.add(user1)
        answer1.save()
        answer2=Answer.objects.create(text=RichTextField("Why dont you try using bertands theorem"), author=user3, anonymous=True, pub_date=datetime(2020,1,1,1,1,3,tzinfo=pytz.UTC),to_question=question1)
        answer2.dislikedBy.add(user1)
        answer2.save()

    def test_content_richfield(self):
        answer = Answer.objects.all()[0]
        expected_object_name =answer.text
        self.assertEqual(str(RichTextField("Why dont yu try using bertands theorem")), expected_object_name)

    def test_likedBy_check(self):
        answer = Answer.objects.all()[0]
        expected_object_name = answer.likedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)
    
    def test_dislikedBy_check(self):
        answer = Answer.objects.all()[1]
        expected_object_name = answer.dislikedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)

    def test_check_author(self):
        answer = Answer.objects.all()[0]
        expected_object_name = answer.author.username
        self.assertEqual("eg2", expected_object_name)

    def test_check_anonymous(self):
        answer = Answer.objects.all()[1]
        expected_object_name = answer.anonymous
        self.assertEqual(expected_object_name, True)

    def test_get_author_name(self):
        answer1 = Answer.objects.all()[0]
        expected_object_name = answer1.get_author_name()
        self.assertEqual(expected_object_name, 'harish2')
        answer2 = Answer.objects.all()[1]
        expected_object_name = answer2.get_author_name()
        self.assertEqual(expected_object_name, 'Anonymous User')
    
    def test_vote_count(self):
        answer = Answer.objects.all()[0]
        expected_object_name = answer.likedBy.count()-answer.dislikedBy.count()
        self.assertEqual(expected_object_name, 1)

    