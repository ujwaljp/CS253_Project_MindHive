from django.test import TestCase
from questions.models import Question
from ckeditor.fields import RichTextField
from users.models import User
from datetime import datetime
from tags.models import Tag
import pytz
class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        text_content=RichTextField("So I have a question")
        user1 = User(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        user2 = User(email="example2@iitk.ac.in", username="eg2", password="example2",name="harish2")
        user3 = User(email="example3@iitk.ac.in", username="eg3", password="example3",name="harish3")
        tag=Tag.objects.create(name="tag1")
        user1.save()
        user2.save()
        user3.save()
        question1=Question.objects.create(text=text_content, author=user1, anonymous=False, pub_date=datetime(2020,1,1,0,0,0,tzinfo=pytz.UTC),title="How to do this?")
        question2=Question.objects.create(text=text_content, author=user2, anonymous=True, pub_date=datetime(2020,1,1,1,1,1,tzinfo=pytz.UTC),title="I am anonymous")
        question1.likedBy.add(user1)
        question1.likedBy.add(user3)
        question1.dislikedBy.add(user2)
        question1.viewedBy.add(user1)
        question1.tags.add(tag)
        question1.save()
        question2.save()
    def test_title_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_question_name(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.title
        self.assertEqual(str(question), expected_object_name)

    def test_content_richfield(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.text
        self.assertEqual(str(RichTextField("So I have a question")), expected_object_name)
    
    def test_tag_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.tags.get(id=1).name
        self.assertEqual("tag1", expected_object_name)

    def test_likedBy_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.likedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)

    def test_dislikedBy_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.dislikedBy.get(id=2).username
        self.assertEqual("eg2", expected_object_name)

    def test_viewedby_check(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.viewedBy.get(id=1).username
        self.assertEqual("eg", expected_object_name)

    def test_check_author(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.author.username
        self.assertEqual("eg", expected_object_name)

    def test_check_anonymous(self):
        question = Question.objects.get(id=2)
        expected_object_name = question.anonymous
        self.assertEqual(expected_object_name, True)

    def test_get_author_name(self):
        question1 = Question.objects.get(id=1)
        expected_object_name = question1.get_author_name()
        self.assertEqual(expected_object_name, 'harish')
        question2 = Question.objects.get(id=2)
        expected_object_name = question2.get_author_name()
        self.assertEqual(expected_object_name, 'Anonymous User')

    def test_get_absolute_url(self):
        question = Question.objects.get(id=2)
        expected_object_name = question.get_absolute_url()
        self.assertEqual(expected_object_name, '/questions/2')
    
    def test_get_votes(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.get_votes()
        self.assertEqual(expected_object_name, 1)

    