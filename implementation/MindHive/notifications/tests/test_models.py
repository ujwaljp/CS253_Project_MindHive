from django.test import TestCase
from questions.models import Question
from notifications.models import Notification
from users.models import User
from tags.models import Tag
from ckeditor.fields import RichTextField
from datetime import datetime
import pytz
class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        text_content=RichTextField("So I have a question")
        notification1 = Notification.objects.create(text="This question has been answered by sharma ji")
        user1 = User.objects.create(email="example@iitk.ac.in", username="eg", password="example",name="harish")
        user2 = User.objects.create(email="example2@iitk.ac.in", username="eg2", password="example2",name="harish2")
        user3 = User.objects.create(email="example3@iitk.ac.in", username="eg3", password="example3",name="harish3")
        question1=Question.objects.create(text=text_content, author=user1, anonymous=False, pub_date=datetime(2020,1,1,0,0,0,tzinfo=pytz.UTC),title="How to do this?")
        tag=Tag.objects.create(name="tag1")
        question1.likedBy.add(user1)
        question1.likedBy.add(user3)
        question1.dislikedBy.add(user2)
        question1.viewedBy.add(user1)
        question1.tags.add(tag)
        notification1.receivers.add(user2)
        notification1.receivers.add(user3)
        notification1.target_question=question1
        notification1.save()
        question1.save()

    def test_text_max_length(self):
        notification =  Notification.objects.get(id=1)
        max_length = notification._meta.get_field('text').max_length
        self.assertEqual(max_length, 200)
    
    def test_text_content(self):
        notification =  Notification.objects.get(id=1)
        self.assertEqual(str(notification), "This question has been answered by sharma ji")

    def test_timestamp_content(self):
        notification =  Notification.objects.get(id=1)
        self.assertEqual(notification.timestamp.date(),datetime.now().date())

    def test_receivers_content(self):
        notification =  Notification.objects.get(id=1)
        value_recieved = notification.receivers.all()[0].username
        self.assertEqual(value_recieved, "eg2")

    def test_target_questions(self):
        notification =  Notification.objects.get(id=1)
        value_recieved = notification.target_question.title
        self.assertEqual(value_recieved, "How to do this?")
    
    
