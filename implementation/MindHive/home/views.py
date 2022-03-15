from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
from users.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='users:login')
def view(request):
    user = User.objects.filter(id = request.user.id).values_list('favouriteTags')
    interestQues = Question.objects.filter(tags__in = user)
    print(interestQues)
    # return HttpResponse(interestQues)
    return render(request, 'home/home.html', {'questions' : interestQues})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Question.object.all().filter(title=search)
        return render(request, 'searchbar.html', {'post':post})
