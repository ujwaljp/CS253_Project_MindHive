from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question_for_polls,Choice
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import CreateQuestionForm    
def index(request):
    latest_question_list = Question_for_polls.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls_list.html', context)

def detail(request, question_id):
    try:
        question = Question_for_polls.objects.get(pk=question_id)
    except Question_for_polls.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question_for_polls, pk=question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question_for_polls, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class QuestionforpollCreateView(CreateView):
    """create a question view"""
    model = Question_for_polls
    form_class = CreateQuestionForm
    template_name = "makepoll.html"

    def get_initial(self):
        """initial data for the form"""
        return {"author": self.request.user.id}

    def get_success_url(self):
        """redirect to the question page on success"""
        return reverse('polls:detail', args=[self.object.id])