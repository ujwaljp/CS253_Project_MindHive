from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
from users.models import User
# Create your views here.
def view(request, user_id):
    user = User.objects.filter(id = user_id).values_list('favouriteTags')
    interestQues = Question.objects.filter(tags__in = user)
    # return HttpResponse(interestQues)
    return render(request, 'home/home.html', {'questions' : interestQues})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Question.object.all().filter(title=search)
        return render(request, 'searchbar.html', {'post':post})