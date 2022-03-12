import re
from django.shortcuts import redirect, render
from users.models import User
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
    roll_no=request.POST['roll_no']
    # check if the both the passwords are same
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        msg = ['An account with the given Username/Email already exists']
        return render(request, 'sign_up.html', {'errors' : msg})
    elif password != password2:
        msg = ["Passwords don't match"]
        return render(request, 'sign_up.html', {'errors' : msg})
        
    if password == password2:
        new_user = User.objects.create(username=username, password=password,name=name, email=email ,roll_no=roll_no)
        new_user.save()
        return redirect('/')