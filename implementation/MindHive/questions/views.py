from django.http import HttpResponse
from django.shortcuts import render

from questions.models import Question

def view(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'questions/view_ques.html', {'question': question})

def edit(request, question_id):
    return HttpResponse("You're editing question %s." % question_id)

def ask(request):
    return HttpResponse("You're asking a question.")