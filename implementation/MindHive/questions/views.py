import json
import sys
import re

from .forms import CreateQuestionForm, AddAnswerForm, CreateReportForm
from .models import Question
from answers.models import Answer
from comments.models import Comment
from notifications.models import Notification

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

sys.path.append("..")


def view_question(request, question_id):
    """view question page"""
    # if user is not authenticated, redirect to login page
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    question = get_object_or_404(Question, id=question_id)

    # if user is visting the question for first time, add to visited questions
    if not question.viewedBy.filter(id=request.user.id).exists():
        question.viewedBy.add(request.user.id)

    # initial data for the answer form
    initial_ans_data = {
        'author': request.user,
        'to_question': question
    }
    # context for the template
    context = {
        'question': question,
        'user': request.user,
        'form': AddAnswerForm(initial_ans_data),
    }

    # if there exists a notification for the user referring to the given question, delete it
    for notif in request.user.notifications.filter(target_question=question):
        notif.receivers.remove(request.user.id)

        # if no receivers left, delete the notification
        if notif.receivers.count() == 0:
            notif.delete()

    return render(request, 'questions/view_ques.html', context)


def edit_question(request, question_id):
    """edit question view"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    # for POST request (on submit)
    if request.method == 'POST':
        question = get_object_or_404(Question, id=question_id)
        form = CreateQuestionForm(request.POST, instance=question)
        
        # if form is valid, save it
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))
        
        # if form is not valid, return the form with errors
        else:
            context = {
                'question': question,
                'user': request.user,
                'form': form
            }
            return render(request, 'questions/askform.html', context)

    # for GET request
    question = get_object_or_404(Question, id=question_id)
    form = CreateQuestionForm(instance=question)
    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'questions/askform.html', context=context)


def vote(request, question_id):
    """vote for question, answer or comment"""
    if not request.user.is_authenticated:  # add blocked as well
        return HttpResponseRedirect(reverse('users:login'))

    if request.POST['obj_type'] == 'question':
        object = get_object_or_404(Question, id=request.POST['obj_id'])
    elif request.POST['obj_type'] == 'answer':
        object = get_object_or_404(Answer, id=request.POST['obj_id'])
    elif request.POST['obj_type'] == 'comment':
        object = get_object_or_404(Comment, id=request.POST['obj_id'])
    else:
        raise Http404

    user = request.user
    vote = request.POST['vote']
    liked = object.likedBy.filter(id=user.id).exists()
    disliked = object.dislikedBy.filter(id=user.id).exists()
    status = "none"    # final status of the object (liked, disliked, none)

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

    # json data to change the vote count without reloading the webpage
    json_data = {
        'likes': object.likedBy.count(),
        'dislikes': object.dislikedBy.count(),
        'obj_type': request.POST['obj_type'],
        'votes': object.likedBy.count() - object.dislikedBy.count(),
        'status': status
    }
    return HttpResponse(json.dumps(json_data))


def follow_bookmark(request):
    """follow or bookmark a question"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    user = request.user
    question = get_object_or_404(Question, id=request.POST['question_id'])
    action = request.POST['action']

    if action == 'bookmark':
        if user in question.users_bookmarked.all():
            question.users_bookmarked.remove(user.id)
            status = 'unbookmarked'
        else:
            question.users_bookmarked.add(user.id)
            status = 'bookmarked'
    else:
        if user in question.users_following.all():
            question.users_following.remove(user.id)
            status = 'unfollowed'
        else:
            question.users_following.add(user.id)
            status = 'followed'

    return HttpResponse(json.dumps({'status': status}))


def add_comment(request, question_id):
    """add comment to a question or answer"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    user = request.user

    if request.POST['obj_type'] == 'question':
        object = get_object_or_404(Question, id=request.POST['question_id'])
        parentObjQ = object
        parentObjA = None
        send_notification(
            'commentQ', request.POST['question_id'], question_id, user.name, user.id)
    else:
        object = get_object_or_404(Answer, id=request.POST['answer_id'])
        parentObjQ = None
        parentObjA = object
        send_notification(
            'commentA', request.POST['answer_id'], question_id, user.name, user.id)
    
    object.comment_set.create(
        text=request.POST['comment_text'],
        author=user,
        parentObjType=request.POST['obj_type'][0],
        parentObjQ=parentObjQ,
        parentObjA=parentObjA
    )
    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


def add_answer(request, question_id):
    """add answer to a question"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    form = AddAnswerForm(request.POST, use_required_attribute=False)
    if form.is_valid():
        form.save()

        # send a notification to the question author and all the users who follow the question
        author = Answer.objects.get(id=form.instance.id).get_author_name()
        author_id = Answer.objects.get(id=form.instance.id).author.id
        send_notification('answer', form.instance.id,
                          question_id, author, author_id)

    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


def send_notification(objType, objId, question_id, author, author_id):
    """send notification to all the users who follow the question"""

    target_question = Question.objects.get(pk=question_id)
    if objType == 'answer':
        message = author + ' answered the question "' + \
            target_question.title[:25] + '..?"'
        receivers = target_question.users_following.all()
    elif objType == 'commentQ':
        message = author + ' commented on the question "' + \
            target_question.title[:25] + '..?"'
        receivers = target_question.users_following.all()
    elif objType == 'commentA':
        answer = Answer.objects.get(pk=objId)
        message = author + ' commented on your answer "' + \
            answer.text[:25] + '..."'
        receivers = answer.author

    cleanr = re.compile('<.*?>')
    message = re.sub(cleanr, '', message)
    notif = Notification.objects.create(
        text=message, target_question=target_question)

    if objType == 'answer' or objType == 'commentQ':
        for receiver in receivers:
            notif.receivers.add(receiver)
        notif.receivers.add(target_question.author)
    elif objType == 'commentA':
        notif.receivers.add(receivers)

    # no notification for the author of the content
    notif.receivers.remove(author_id)

    # if no receivers, delete the notification
    if notif.receivers.count == 0:
        notif.delete()
    else:
        notif.save()


def report(request, question_id):
    """report a question or answer"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    reportedObjQ = None
    reportedObjA = None
    reportedObjC = None
    if request.POST['obj_type'] == 'q':
        reportedObjQ = get_object_or_404(Question, id=request.POST['id'])
        reportedUser = reportedObjQ.author
    elif request.POST['obj_type'] == 'a':
        reportedObjA = get_object_or_404(Answer, id=request.POST['id'])
        reportedUser = reportedObjA.author
    else:
        reportedObjC = get_object_or_404(Comment, id=request.POST['id'])
        reportedUser = reportedObjC.author

    initial_report_data = {
        'reporter': request.user,
        'report_text': request.POST['report_text'],
        'reportedUser': reportedUser,
        'reportedObjType': request.POST['obj_type'],
        'reportedObjQ': reportedObjQ,
        'reportedObjA': reportedObjA,
        'reportedObjC': reportedObjC,
    }
    form = CreateReportForm(initial_report_data)
    form.save()
    return HttpResponseRedirect(reverse('questions:view_question', args=[question_id]))


class QuestionCreateView(CreateView):
    """create a question view"""
    model = Question
    form_class = CreateQuestionForm
    template_name = "questions/askform.html"

    def get_initial(self):
        """initial data for the form"""
        return {"author": self.request.user.id}

    def get_success_url(self):
        """redirect to the question page on success"""
        return reverse('questions:view_question', args=[self.object.id])
