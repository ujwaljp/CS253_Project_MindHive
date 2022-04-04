from django.test import TestCase
from users.models import User
from tags.models import Tag
from answers.models import Answer
from ckeditor.fields import RichTextField
from datetime import datetime
from questions.models import Question
from comments.models import Comment
import pytz

class CommentModelTest(TestCase):
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
        comment1=Comment.objects.create(text=RichTextField("What is bertands theorem?"), author=user1, anonymous=False, pub_date=datetime(2020,1,1,1,1,5,tzinfo=pytz.UTC),parentObjType="a",parentObjA=answer1)
        comment2=Comment.objects.create(text=RichTextField("I will report this question."), author=user2, anonymous=True, pub_date=datetime(2020,1,1,1,1,7,tzinfo=pytz.UTC),parentObjType="q",parentObjQ=question1)
        
    def test_text_content(self):
        comment=Comment.objects.all()[0]
        expected_object_name =comment.text
        self.assertEqual(expected_object_name, str(RichTextField("What is bertands theorem?")))
        
    def test_author_username(self):
        comment=Comment.objects.all()[0]
        expected_object_name =comment.author.username
        self.assertEqual(expected_object_name, "eg")
        
    def test_check_anonymous(self):
        comment=Comment.objects.all()[1]
        expected_object_name =comment.anonymous
        self.assertEqual(expected_object_name, True)
        
        
    def test_parentObjTypeQ(self):
        comment=Comment.objects.all()[1]
        expected_object_name =comment.parentObjType
        self.assertEqual(expected_object_name, "q")
    
    def test_parentObjTypeA(self):
        comment=Comment.objects.all()[0]
        expected_object_name =comment.parentObjType
        self.assertEqual(expected_object_name, "a")  
        
    def test_parentObjQ(self):
        comment=Comment.objects.all()[1]
        expected_object_name =comment.parentObjQ.title
        self.assertEqual(expected_object_name, "How to do this?")
    
    def test_parentObjA(self):
        comment=Comment.objects.all()[0]
        expected_object_name =comment.parentObjA.text
        self.assertEqual(expected_object_name, str(RichTextField("Why dont you try using bertands theorem")))
        
    def test_get_author_name(self):
        comment=Comment.objects.all()[0]
        expected_object_name =comment.get_author_name()
        self.assertEqual(expected_object_name, "harish")
        
        anonymous_comment=Comment.objects.all()[1]
        expected_object_name=anonymous_comment.get_author_name()
        self.assertEqual(expected_object_name, "Anonymous User")
        
    
        
        
    


