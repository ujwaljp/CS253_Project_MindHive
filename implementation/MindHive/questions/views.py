from django.http import HttpResponse
import sys
sys.path.append("..")
from .models import Question
from users.models import User
from django.shortcuts import render, get_object_or_404
import datetime
def view(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'questions/view_ques.html', {'question': question})

def edit(request, question_id):
    return HttpResponse("You're editing question %s." % question_id)

def ask(request, user_id):
    return render(request, 'questions/ask.html')

def submit(request, user_id):
    # user = User.objects.filter(id = user_id).values('User')
    user = get_object_or_404(User, id = user_id)
    newQuestion = Question.objects.create(text = request.POST.get('question',False), pub_date = datetime.datetime.now(), author = user)
    return render(request, 'questions/submit.html', {'Ques' : newQuestion})