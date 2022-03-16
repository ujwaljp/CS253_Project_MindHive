import json
import sys

from .forms import CreateQuestionForm, AddAnswerForm, CreateReportForm
from .models import Question
from answers.models import Answer
from comments.models import Comment
from users.models import Report

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

sys.path.append("..")


def view_question(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    question = get_object_or_404(Question, id=question_id)
    if not question.viewedBy.filter(id=request.user.id).exists():
        question.viewedBy.add(request.user.id)

    initial_ans_data = {
        'author': request.user,
        'to_question': question
    }
    context = {
        'question': question,
        'user': request.user,
        'form': AddAnswerForm(initial_ans_data),
    }
    return render(request, 'questions/view_ques.html', context)


def edit_question(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    if request.method == 'POST':
        question = get_object_or_404(Question, id=question_id)
        form = CreateQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))

    # for GET request
    question = get_object_or_404(Question, id=question_id)
    form = CreateQuestionForm(instance=question)
    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'questions/askform.html', context=context)


def vote(request, question_id):
    if not request.user.is_authenticated:  # add blocked as well
        return HttpResponseRedirect(reverse('users:login'))
    
    if request.POST['obj_type'] == 'question':
        object = get_object_or_404(Question, id=request.POST['obj_id'])
    else:
        object = get_object_or_404(Answer, id=request.POST['obj_id'])
    
    user = request.user
    vote = request.POST['vote']
    liked = object.likedBy.filter(id=user.id).exists()
    disliked = object.dislikedBy.filter(id=user.id).exists()
    status = "none"

    if vote == 'upvote':
        if liked:
            object.likedBy.remove(user.id)
        else:
            object.likedBy.add(user.id)
            status = 'liked'
            if disliked:
                object.dislikedBy.remove(user.id)
    else:
        if disliked:
            object.dislikedBy.remove(user.id)
        else:
            object.dislikedBy.add(user.id)
            status = 'disliked'
            if liked:
                object.likedBy.remove(user.id)

    json_data = {
        'likes': object.likedBy.count(),
        'dislikes': object.dislikedBy.count(),
        'status': status
    }
    return HttpResponse(json.dumps(json_data))


def follow_bookmark(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
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
    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


def add_comment(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
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
    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


def add_answer(request, question_id):
    form = AddAnswerForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


def report(request, question_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    if request.method == 'POST':
        form = CreateReportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))
    
    reportedObjQ = None
    reportedObjA = None
    reportedObjC = None
    if request.GET['obj_type'] == 'q':
        reportedObjQ = get_object_or_404(Question, id=request.GET['id'])
        reportedUser = reportedObjQ.author
    elif request.GET['obj_type'] == 'a':
        reportedObjA = get_object_or_404(Answer, id=request.GET['id'])
        reportedUser = reportedObjA.author
    else:
        reportedObjC = get_object_or_404(Comment, id=request.GET['id'])
        reportedUser = reportedObjC.author

    initial_report_data = {
        'reporter': request.user,
        'reportedUser': reportedUser,
        'reportedObjType': request.GET['obj_type'],
        'reportedObjQ': reportedObjQ,
        'reportedObjA': reportedObjA,
        'reportedObjC': reportedObjC,
    }
    form = CreateReportForm(initial_report_data)
    context = {
        'question_id': question_id,
        'form': form,
    }
    return render(request, 'questions/report.html', context=context)


class QuestionCreateView(CreateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = "questions/askform.html"
    success_url = 'https://stackoverflow.com/a/60273100/7063031'

    def get_initial(self):
        return {"author": self.request.user.id}


def ajax_posting(request):
    response = {
        'msg':'Your form has been submitted successfully' # response message
    }
    if not request.user.is_authenticated:  # add blocked as well
        return HttpResponseRedirect(reverse('users:login'))
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
