import profile
from django import forms
from .models import User
import sys
sys.path.append("..")

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from tags.models import Tag

# form for signing up
class UserCreateForm(UserCreationForm):
    class Meta:
        # declare the approproate fields
        fields = ('username', 'name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

# form for editing the username and the profile image
class UpdateUserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","profile_image"]
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your new user name'}),
        }
        profile_image=forms.ImageField()

# form for adding the favourite tags
class addTagsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['favouriteTags']
        widgets = []
        favouriteTags = forms.ModelMultipleChoiceField(
                        queryset=Tag.objects.all(),
                        widget=forms.CheckboxSelectMultiple)


# class CreateQuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ["title","text","tags","author"]
#         title = forms.CharField()
#
#         tags = forms.ModelMultipleChoiceField(
#             queryset=Tag.objects.all(),
#             widget=forms.CheckboxSelectMultiple,
#         )
