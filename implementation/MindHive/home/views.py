from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from questions.models import Question
from users.models import User
from tags.models import Tag
from django.contrib.auth.decorators import login_required
from questions.models import Question
from django.db.models import Q


# only show the below views to logged in users
# if not logged in, redirect to login page
@login_required(login_url='users:login')
def view(request):
    """home page view"""
    user = User.objects.filter(id=request.user.id).values_list('favouriteTags')
    if not (user.first()==(None,)):
        interestQues = Question.objects.filter(tags__in=user).distinct()
    else:
        interestQues = Question.objects.filter(tags__in=get_popular_tags()).distinct()
    context = {
        'questions': interestQues,
        'pop_tags': get_popular_tags()
    }
    #return HttpResponse((user.first()==(None,)))
    return render(request, 'home/home.html', context=context)


def bookView(request):
    """bookmarks page view"""
    user = User.objects.filter(
        id=request.user.id).values_list('bookmarkQuestions')
    bookQuestions = Question.objects.filter(id__in=user).distinct()
    context = {
        'questions': bookQuestions,
        'pop_tags': get_popular_tags()
    }
    return render(request, 'home/bookmark_questions.html', context=context)


def folView(request):
    """following page view"""
    user = User.objects.filter(
        id=request.user.id).values_list('followingQuestions')
    folQuestions = Question.objects.filter(id__in=user).distinct()
    context = {
        'questions': folQuestions,
        'pop_tags': get_popular_tags()
    }
    return render(request, 'home/follow_questions.html', context=context)


def allQuestionsView(request):
    """all questions page view"""
    questions = Question.objects.all()
    context = {
        'questions': questions,
        'pop_tags': get_popular_tags()
    }
    return render(request, 'home/questions.html', context=context)


def tagView(request, tagname):
    """tag questions page view"""
    tagSel = Tag.objects.filter(name=tagname)
    tagQues = Question.objects.filter(tags__in=tagSel).distinct()
    context = {
        'questions': tagQues,
        'pop_tags': get_popular_tags()
    }
    return render(request, 'home/home.html', context=context)


def autQues(request):
    """author questions page view"""
    user = User.objects.filter(id=request.user.id)
    autQuestions = Question.objects.filter(author__in=user).distinct()
    context = {
        'questions': autQuestions,
        'pop_tags': get_popular_tags(),
        'title': 'My Questions'
    }
    return render(request, 'home/author_questions.html', context=context)

def otautQues(request, user_id):
    """author questions page view"""
    user = User.objects.filter(id=user_id)
    autQuestions = Question.objects.filter(author__in=user,anonymous=False).distinct()
    context = {
        'questions': autQuestions,
        'pop_tags': get_popular_tags(),
        'title': 'Questions asked by '+user.first().name
    }
    return render(request, 'home/author_questions.html', context=context)

def search_results(request):
    """search results page view"""
    searched = request.GET['searched']
    # check if searched query is non empty
    if searched:
        searched_ques = Question.objects.filter(
            Q(title__icontains=searched) | Q(text__icontains=searched)).distinct()
        context = {
            "searched": searched,
            "questions": searched_ques,
            'pop_tags': get_popular_tags()
        }
        return render(request, 'home/search_results.html', context=context)
    else:
        return render(request, 'base.html')


def get_popular_tags():
    """return popular tags"""
    return sorted(Tag.objects.all(), key=lambda x: x.question_set.count(), reverse=True)[:10]
