from django import forms
from .models import Question
import sys
sys.path.append("..")
from tags.models import Tag
from ckeditor.fields import RichTextField,RichTextFormField
class CreateQuestionForm(forms.ModelForm):    
    class Meta:
        model = Question
        fields = ["title","text","tags","author"] 
        title = forms.CharField()  
        widgets = {'author': forms.HiddenInput(),'text':RichTextFormField()}  
        tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        )
