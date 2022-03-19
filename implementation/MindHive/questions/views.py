from email import message
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
from users.models import User
from notifications.models import Notification

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
    for notif in request.user.notifications.filter(target_question=question):
        notif.receivers.remove(request.user.id)
        if notif.receivers.count() == 0:
            notif.delete()
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
        send_notification('commentQ', request.POST['question_id'], question_id, user.name, user.id)
    else:
        object = get_object_or_404(Answer, id=request.POST['answer_id'])
        parentObjQ = None
        parentObjA = object
        send_notification('commentA', request.POST['answer_id'], question_id, user.name, user.id)
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
        author = Answer.objects.get(id=form.instance.id).get_author_name()
        author_id = Answer.objects.get(id=form.instance.id).author.id
        send_notification('answer', form.instance.id, question_id, author, author_id)
    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


def send_notification(objType, objId, question_id, author, author_id):
    target_question = Question.objects.get(pk=question_id)
    if objType == 'answer':
        message = author + ' answered the question "' + target_question.title[:25] + '..?"'
        receivers = target_question.users_following.all()
    elif objType == 'commentQ':
        message = author + ' commented on the question "' + target_question.title[:25] + '..?"'
        receivers = target_question.users_following.all()
    elif objType == 'commentA':
        answer = Answer.objects.get(pk=objId)
        message = author + ' commented on your answer "' + answer.text[:25] + '..."'
        receivers = answer.author
    
    notif = Notification.objects.create(text=message, target_question=target_question)
    if objType == 'answer' or objType == 'commentQ':
        for receiver in receivers:
            notif.receivers.add(receiver)
        notif.receivers.add(target_question.author)
    elif objType == 'commentA':
        notif.receivers.add(receivers)
    notif.receivers.remove(author_id)
    if notif.receivers.count == 0:
        notif.delete()
    else:
        notif.save()


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
    # success_url = reverse('questions:view_question', args=[self.object.id])

    def get_initial(self):
        return {"author": self.request.user.id}
    def get_success_url(self):
        return reverse('questions:view_question', args=[self.object.id])

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
