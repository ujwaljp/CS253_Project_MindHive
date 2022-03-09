from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def view(request):
    usr1 = User()
    usr1.username = 'ujp'
    usr1.name = 'Ujwal'
    usr1.email = 'ujwaljp20'
    usr1.password = 'ggopwp'
    usr1.blocked = False
    usr = [usr1]
    # return render(request, 'profile.html', {'users': usr})
    return HttpResponse("Hello, world. You're at the polls index.")
def edit(request):
    # return render(request, 'profile.html', {'users': usr})
    return HttpResponse("Here the edit page will come")