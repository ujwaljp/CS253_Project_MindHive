from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def profile(request,user_id):
    usr = User.objects.get(id=user_id)
    return render(request, 'homepage.html', {'usr': usr})

def edit(request):
    return HttpResponse("Here the edit page will come")
