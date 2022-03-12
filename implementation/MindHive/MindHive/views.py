## Login page for new/tokenless user ## 

import re
from django.shortcuts import redirect, render
from users.models import User
from 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'sign_up.html')

def createuser(request):
    username = request.POST['username']
    password = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    name = request.POST['name']
    # check if the both the passwords are same
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        msg = ['An account with the given Username/Email already exists']
        return render(request, 'sign_up.html', {'errors' : msg})
    elif password != password2:
        msg = ["Passwords don't match"]
        return render(request, 'sign_up.html', {'errors' : msg})
        
    if password == password2:
        # email auth part here
        new_user = User.objects.create(username=username, password=password,name=name, email=email )
        new_user.save()
        return redirect('/')