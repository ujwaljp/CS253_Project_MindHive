from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
from answers.models import Answer
from users.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
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
#
# class HomeView(generic.ListView):
#     model = Question
#     template_name = 'home/home.html'
#
#     def get_query_set(self):
#         try:
#             self.fav_questions = Questions.objects.filter()

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Question.object.all().filter(title=search)
        return render(request, 'searchbar.html', {'post':post})
