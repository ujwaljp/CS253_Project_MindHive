import sys

from users.models import Report
sys.path.append("..")

from django import forms
from tags.models import Tag
from answers.models import Answer
from .models import Question

from ckeditor.fields import RichTextFormField

class CreateQuestionForm(forms.ModelForm):    
    class Meta:
        model = Question
        fields = ["title","text","tags","author"] 
        title = forms.CharField()  
        widgets = {
            'author': forms.HiddenInput(),
            'text': RichTextFormField()
        }  
        tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )

class AddAnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].initial = ' '
        self.fields['author'].initial = 'author'
        self.fields['to_question'].initial = 'to_question'

    class Meta:
        model = Answer
        fields = ["text", "author", "anonymous", "to_question"]
        widgets = {
            'text': RichTextFormField(),
            'author': forms.HiddenInput(),
            'to_question': forms.HiddenInput(),
        }
        labels = {
            'text': '',
            'anonymous': 'Answer anonymously?',
        }
        anonymous = forms.BooleanField(required=False)


# class CreateReportForm(forms.ModelForm):
#     class Meta:
#         model = Report
