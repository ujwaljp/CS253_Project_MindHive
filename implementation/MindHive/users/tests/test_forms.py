from django import forms
from django.test import TestCase
from matplotlib import widgets
from questions.models import Question
from notifications.models import Notification
from users.forms import *
from users.models import User
from tags.models import Tag
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
import pytz

# class Setup_Class(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(email="user@iitk.ac.in", username="user", password="cscbndm",name="user")
#         user1 = User(email="example@iitk.ac.in", username="eg", password="example",name="harish")
#         user1.save()
#         # question = Question.objects.create(title='test',tags='Anarchy')

class UserCreateFormTest(TestCase):
    def test_valid(self):
        form_data = {'username': 'user',
                     'name': 'user',
                     'email': 'user@iitk.ac.in',
                     'password1':'Cscbndm01$5',
                     'password2':'Cscbndm01$5'}
        form = UserCreateForm(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.username, "user")
        self.assertEqual(saved.name, "user")
        self.assertEqual(saved.email,"user@iitk.ac.in")
        
class UpdateUserInfoTest(TestCase):
    def test_valid(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=open('media/profile_image/index.jpeg', 'rb').read(), content_type='image/jpeg')
        form_data = {'username': 'user',
                     'profile_image': image
                     }
        form = UpdateUserInfo(data = form_data)
        self.assertTrue(form.is_valid())
        saved = form.save()
        self.assertEqual(saved.username, "user")
        # self.assertEqual(saved.profile_image, image)
