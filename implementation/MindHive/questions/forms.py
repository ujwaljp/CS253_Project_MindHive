from django import forms
from .models import Question
import sys
sys.path.append("..")
from tags.models import Tag
class CreateQuestionForm(forms.ModelForm):    
    class Meta:
        model = Question
        fields = ["title","text","tags","author"] 
        title = forms.CharField()  
        widgets = {'author': forms.HiddenInput()}  
        tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )
