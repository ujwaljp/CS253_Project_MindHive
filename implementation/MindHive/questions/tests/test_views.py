from datetime import datetime
import pytz
from ckeditor.fields import RichTextField


from django.test import TestCase
from django.urls import reverse

from answers.models import Answer
from comments.models import Comment
from questions.models import Question
from tags.models import Tag
from users.models import User


def create_dummy_data():
    # create dummy users
    user1 = User.objects.create(
        email="example@iitk.ac.in", username="eg", password="example", name="name1 surname1")
    user2 = User.objects.create(
        email="example2@iitk.ac.in", username="eg2", password="example2", name="name2 surname2")
    user3 = User.objects.create(
        email="example3@iitk.ac.in", username="eg3", password="example3", name="name3")

    # create dummy tags
    tag1 = Tag.objects.create(name="tag1")
    tag2 = Tag.objects.create(name="tag2")

    # create dummy questions
    question_text = RichTextField("A question created for testing.")
    question = Question.objects.create(text=question_text, author=user1, anonymous=False, pub_date=datetime(
        2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC), title="This is a test question.")

    question.likedBy.add(user1, user2)
    question.dislikedBy.add(user3)
    question.viewedBy.add(user1, user2, user3)
    question.tags.add(tag1, tag2)
    question.save()

    # create dummy answer
    answer_text = RichTextField("An answer created for testing.")
    answer = Answer.objects.create(text=answer_text, author=user1, to_question=question, pub_date=datetime(
        2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
    answer.likedBy.add(user1)
    answer.dislikedBy.add(user3)
    answer.save()

    # create dummy comments
    comment_text1 = RichTextField(
        "A comment on question created for testing.")
    comment_text2 = RichTextField(
        "A comment on question created for testing.")
    Comment.objects.create(text=comment_text1, author=user2, parentObjType='q', parentObjQ=question, pub_date=datetime(
        2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
    Comment.objects.create(text=comment_text2, author=user3, parentObjType='a', parentObjA=answer, pub_date=datetime(
        2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))



class QuestionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertEqual(response.status_code, 200)
