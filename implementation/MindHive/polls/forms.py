from .models import Question_for_polls,Choice
import sys
sys.path.append("..")
from django import forms
from tags.models import Tag
from ckeditor.fields import RichTextFormField

class CreateQuestionForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = True  
    class Meta:
        model = Question_for_polls
        fields = ["title","text","tags","author","anonymous"]
        labels = {"anonymous" : "Ask Anonymously?"} 
        title = forms.CharField(max_length=100)
        widgets = {
            'author': forms.HiddenInput(),
            'text': RichTextFormField(),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input form-check-inline',
                }),
        }
        anonymous = forms.BooleanField(required=False)
class AddChoicesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice_text'].initial = ' '
        self.fields['question'].initial = 'question'

    class Meta:
        model = Choice
        fields = ["choice_text", "question"]
        widgets = {
            'question': forms.HiddenInput(),
        }
        labels = {
            'choice_text': '',
        }