from tkinter import NONE
from django.http import HttpResponse
from django.shortcuts import render
from django.test import tag
from questions.models import Question
from users.models import User
from tags.models import Tag
from django.contrib.auth.decorators import login_required
from questions.models import Question
from django.db.models import Q
from django.contrib import messages
# Create your views here.


@login_required(login_url='users:login')
def view(request):
    user = User.objects.filter(id=request.user.id).values_list('favouriteTags')
    interestQues = Question.objects.filter(tags__in=user).distinct()
    # ans = []
    # mostLikedAns = []
    # for ques in interestQues:
    #     mostLikedAns.append(Answer.obects.filter())
    # # mostLikedAns= Answer.objects.filter(to_question=)
    # for ques in interestQues:
    #     ans.append(Answer.objects.filter(to_question=question).distinct()[0])
    # print(user)
    # print(interestQues[0].id, interestQues[1].id)
    # return HttpResponse(interestQues)
    return render(request, 'home/home.html', {'questions': interestQues, 'pop_tags': get_popular_tags()})


def bookView(request):
    user = User.objects.filter(
        id=request.user.id).values_list('bookmarkQuestions')
    bookQuestions = Question.objects.filter(id__in=user).distinct()
    # Creturn HttpResponse(user)
    return render(request, 'home/bookmark_questions.html', {'questions': bookQuestions, 'pop_tags': get_popular_tags()})


def folView(request):
    user = User.objects.filter(
        id=request.user.id).values_list('followingQuestions')
    folQuestions = Question.objects.filter(id__in=user).distinct()
    # Creturn HttpResponse(user)
    return render(request, 'home/follow_questions.html', {'questions': folQuestions, 'pop_tags': get_popular_tags()})


def allQuestionsView(request):
    questions = Question.objects.all()
    return render(request, 'home/questions.html', {'questions': questions, 'pop_tags': get_popular_tags()})


def tagView(request, tagname):
    tagSel = Tag.objects.filter(name=tagname)  # request.POST['tags'])
    tagQues = Question.objects.filter(tags__in=tagSel).distinct()
    return render(request, 'home/home.html', {'questions': tagQues, 'pop_tags': get_popular_tags()})


def autQues(request):
    user = User.objects.filter(id=request.user.id)
    autQuestions = Question.objects.filter(author__in=user).distinct()
    return render(request, 'home/home.html', {'questions': autQuestions, 'pop_tags': get_popular_tags()})

# class HomeView(generic.ListView):
#     model = Question
#     template_name = 'home/home.html'
#
#     def get_query_set(self):
#         try:
#             self.fav_questions = Questions.objects.filter()


def search_results(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        # q=searched.split()
        if searched:
            searched_ques = Question.objects.filter(
                Q(title__icontains=searched) | Q(text__icontains=searched)).distinct()
            return render(request, 'home/search_results.html', {"searched": searched, 'questions': searched_ques})
        else:
            return render(request, 'base.html')
    else:
        return render(request, 'home/search_results.html')


def get_popular_tags():
    return sorted(Tag.objects.all(), key=lambda x: x.question_set.count(), reverse=True)[:10]
