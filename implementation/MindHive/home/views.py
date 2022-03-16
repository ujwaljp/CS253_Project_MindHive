from django.http import HttpResponse
from django.shortcuts import render
from questions.models import Question
from users.models import User
from django.contrib.auth.decorators import login_required
from questions.models import Question
# Create your views here.
@login_required(login_url='users:login')
def view(request):
    user = User.objects.filter(id = request.user.id).values_list('favouriteTags')
    interestQues = Question.objects.filter(tags__in = user).distinct()
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
    return render(request, 'home/home.html', {'questions' : interestQues})

def bookView(request):
    user = User.objects.filter(id = request.user.id).values_list('bookmarkQuestions')
    bookQuestions = Question.objects.filter(id__in = user).distinct()
    # Creturn HttpResponse(user)
    return render(request, 'home/home.html', {'questions':bookQuestions})

def folView(request):
    user = User.objects.filter(id = request.user.id).values_list('followingQuestions')
    folQuestions = Question.objects.filter(id__in = user).distinct()
    # Creturn HttpResponse(user)
    return render(request, 'home/home.html', {'questions':folQuestions})
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
        posts = Question.objects.all().filter(title__icontains=searched)
        return render(request, 'search_results.html', {'searched':searched, 'posts':posts})
    else:
        return render(request, 'search_results.html', {})