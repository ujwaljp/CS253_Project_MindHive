from sre_constants import SUCCESS
from turtle import title
from urllib import request
from django.http import HttpResponse
from .forms import CreateQuestionForm
import sys
sys.path.append("..")
from .models import Question
from users.models import User
from django.shortcuts import render
from django.views.generic.edit import CreateView
def view(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'questions/view_ques.html', {'question': question})

def edit(request, question_id):
    return HttpResponse("You're editing question %s." % question_id)

class QuestionCreateView(CreateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = "questions/askform.html"
    success_url = 'https://stackoverflow.com/a/60273100/7063031'