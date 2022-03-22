from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import User


# index view
class HomePage(TemplateView):
    template_name = 'index.html'


def createuser(request):
    """create user view"""
    username = request.POST['username']
    password = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    name = request.POST['name']
    roll_no=request.POST['roll_no']

    # if username/email exists in the database, return an error message
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        msg = 'An account with the given Username/Email already exists'
        return render(request, 'sign_up.html', {'errors' : msg})
    
    # check if both the passwords are different
    elif password != password2:
        msg = "Passwords don't match"
        return render(request, 'sign_up.html', {'errors' : msg})

    # if all the conditions are satisfied, create and save new user and redirect to login page
    else:
        new_user = User(username=username, name=name,
                        email=email, roll_no=roll_no)
        new_user.set_password(password)
        new_user.save()
        return render(request, 'index.html')