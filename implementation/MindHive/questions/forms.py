import sys

from users.models import Report
sys.path.append("..")

from django import forms
from tags.models import Tag
from answers.models import Answer
from .models import Question

from ckeditor.fields import RichTextFormField


# form to create a new or edit a question
class CreateQuestionForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = True
    class Meta:
        model = Question
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


# form to create a new or edit an answer
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
            'anonymous': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'text': '',
            'anonymous': 'Answer anonymously?',
        }


# form to create a report
class CreateReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reporter'].initial = 'reporter'
        self.fields['reportedUser'].initial = 'reportedUser'
        self.fields['reportedObjType'].initial = 'reportedObjType'
        self.fields['reportedObjQ'].initial = 'reportedObjQ'
        self.fields['reportedObjA'].initial = 'reportedObjA'
        self.fields['reportedObjC'].initial = 'reportedObjC'
        

    class Meta:
        model = Report
        fields = ["report_text", "reporter", "reportedUser", "reportedObjType",
                  "reportedObjQ", "reportedObjA", "reportedObjC"]
        report_text = forms.CharField(max_length=200)
        labels = {
            'report_text': '',
        }
        widgets = {
            'reporter': forms.HiddenInput(),
            'reportedUser': forms.HiddenInput(),
            'reportedObjType': forms.HiddenInput(),
            'reportedObjQ': forms.HiddenInput(),
            'reportedObjA': forms.HiddenInput(),
            'reportedObjC': forms.HiddenInput(),
        }
