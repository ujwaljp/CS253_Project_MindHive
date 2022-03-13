from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
# Create your views here.
def view(request):
    return HttpResponse("Home page")

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Question.object.all().filter(title=search)
        return render(request, 'searchbar.html', {'post':post})