import sys

from .forms import CreateQuestionForm, AddAnswerForm
from .models import Question
from answers.models import Answer

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

sys.path.append("..")


def view_question(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('view_question', args=[question_id]))
    
    question = get_object_or_404(Question, id=question_id)
    initial_ans_data = {
        'author': request.user,
        'to_question': question
    }
    context = {
        'question': question,
        'user': request.user,
        'bookmarked': question.users_bookmarked.filter(id=request.user.id).exists(),
        'followed': question.users_following.filter(id=request.user.id).exists(),
        'reported': question.report_set.filter(reportedUser=request.user).exists(),
        'form': AddAnswerForm(initial_ans_data),
    }
    return render(request, 'questions/view_ques.html', context)


def edit_question(request, question_id):
    return HttpResponse("You're editing question %s." % question_id)


def vote(request, question_id):
    if not request.user.is_authenticated:  # add blocked as well
        return HttpResponseRedirect(reverse('login'))
    user = request.user
    if request.POST['obj_type'] == 'question':
        object = get_object_or_404(Question, id=question_id)
    else:
        object = get_object_or_404(Answer, id=request.POST['answer_id'])
    vote = request.POST['vote']
    if vote == 'upvote':
        if object.likedBy.filter(id=user.id).exists():
            object.likedBy.remove(user.id)
        else:
            object.likedBy.add(user.id)
            if object.dislikedBy.filter(id=user.id).exists():
                object.dislikedBy.remove(user.id)
    else:
        if object.dislikedBy.filter(id=user.id).exists():
            object.dislikedBy.remove(user.id)
        else:
            object.dislikedBy.add(user.id)
            if object.likedBy.filter(id=user.id).exists():
                object.likedBy.remove(user.id)
    return HttpResponseRedirect(reverse('view_question', args=[question_id]))


def follow_bookmark(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    user = request.user
    question = get_object_or_404(Question, id=question_id)
    action = request.POST['action']
    if action == 'unbookmark':
        question.users_bookmarked.remove(user.id)
    elif action == 'bookmark':
        question.users_bookmarked.add(user.id)
    elif action == 'unfollow':
        question.users_following.remove(user.id)
    elif action == 'follow':
        question.users_following.add(user.id)
    return HttpResponseRedirect(reverse('view_question', args=[question_id]))


def add_comment(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    user = request.user
    if request.POST['obj_type'] == 'question':
        object = get_object_or_404(Question, id=request.POST['question_id'])
        parentObjQ = object
        parentObjA = None
    else:
        object = get_object_or_404(Answer, id=request.POST['answer_id'])
        parentObjQ = None
        parentObjA = object
    object.comment_set.create(
        text = request.POST['comment_text'],
        author = user,
        parentObjType = request.POST['obj_type'][0],
        parentObjQ = parentObjQ,
        parentObjA = parentObjA
    )
    return HttpResponseRedirect(reverse('view_question', args=[question_id]))


class QuestionCreateView(CreateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = "questions/askform.html"
    success_url = 'https://stackoverflow.com/a/60273100/7063031'
    
    def get_initial(self):
        return {"author": self.kwargs.get("user_id")}


def ajax_posting(request):
    response = {
        'msg':'Your form has been submitted successfully' # response message
    }
    if not request.user.is_authenticated:  # add blocked as well
        return HttpResponseRedirect(reverse('login'))
    user = request.user
    if request.POST['obj_type'] == 'question':
        object = get_object_or_404(Question, id=request.POST['question_id'])
    else:
        object = get_object_or_404(Answer, id=request.POST['answer_id'])
    vote = request.POST['vote']
    if vote == 'upvote':
        if object.likedBy.filter(id=user.id).exists():
            object.likedBy.remove(user.id)
        else:
            object.likedBy.add(user.id)
            if object.dislikedBy.filter(id=user.id).exists():
                object.dislikedBy.remove(user.id)
    else:
        if object.dislikedBy.filter(id=user.id).exists():
            object.dislikedBy.remove(user.id)
        else:
            object.dislikedBy.add(user.id)
            if object.likedBy.filter(id=user.id).exists():
                object.likedBy.remove(user.id)
    return JsonResponse(response) # return response as JSON