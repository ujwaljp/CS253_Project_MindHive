import profile
from django import forms
from .models import User
import sys
sys.path.append("..")

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'


class Updateuserinfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","profile_image"]
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your new user name'}),
        }
        profile_image=forms.ImageField()
