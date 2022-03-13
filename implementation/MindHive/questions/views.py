from django.http import HttpResponse
from .forms import CreateQuestionForm
import sys
from .models import Question
from django.shortcuts import render
from django.views.generic.edit import CreateView

sys.path.append("..")

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
    def get_initial(self):
        return {"author": self.kwargs.get("user_id")}