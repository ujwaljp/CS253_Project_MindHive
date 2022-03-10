from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def profile(request,user_id):
    usr = User.objects.get(id=user_id)
    return render(request, 'users/profile.html', {'user': usr})
    #return HttpResponse("Hello, world. You're at the polls index.")

def edit(request):
    # return render(request, 'profile.html', {'users': usr})
    return HttpResponse("Here the edit page will come")
