from django import forms
from .models import Question

class PostForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'text',
            'tags',
        ]