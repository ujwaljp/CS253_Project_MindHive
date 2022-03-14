from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import CreateQuestionForm
import sys
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

sys.path.append("..")

def view(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'questions/view_ques.html', {'question': question})

def edit(request, question_id):
    return HttpResponse("You're editing question %s." % question_id)


def like(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    user_id = 2
    if question.likedBy.filter(id=user_id).exists():
        question.likedBy.remove(user_id)
    else:
        question.likedBy.add(user_id)
        if question.dislikedBy.filter(id=user_id).exists():
            question.dislikedBy.remove(user_id)
    return HttpResponseRedirect(reverse('view_question', args=[question.id]))

def dislike(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    user_id = 2
    if question.dislikedBy.filter(id=user_id).exists():
        question.dislikedBy.remove(user_id)
    else:
        question.dislikedBy.add(user_id)
        if question.likedBy.filter(id=user_id).exists():
            question.likedBy.remove(user_id)
    return HttpResponseRedirect(reverse('view_question', args=[question.id]))

class QuestionCreateView(CreateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = "questions/askform.html"
    success_url = 'https://stackoverflow.com/a/60273100/7063031'
    def get_initial(self):
        return {"author": self.kwargs.get("user_id")}