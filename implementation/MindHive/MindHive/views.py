## Login page for new/tokenless user ## 

import re
from django.shortcuts import redirect, render
from users.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.contrib.auth.models import AbstractUser
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import login, logout

'''
1. How to add password hashing- shouldn't store passwords directly
2. Let's test activation email part for now and disable it, can add it in the end after testing
   the other project components
3. Should we change user model to a one-to-one relationship with the User (default django model)
4. 

'''

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'sign_up.html')

def send_activation_email(user, request):
    current_site = get_current_site(request)
    subject = "Account Confirmation Email" 
    body = render_to_string('Mindhive/activate.html',{
        'user':user,
        'domain': current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.id)),
        'token':generate_token.make_token(user)              #######################################
    })
    
    email = EmailMessage(subject=subject,body=body,
                 from_email=settings.EMAIL_FROM_USER,
                 to=[user.email])
    email.send()

def activate_account(request, uid_b64e, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid_b64e))
        user = User.objects.get(id=uid)
        # ToDo: if no match with uid
    except Exception as e:
        user=None 
    
    if user and generate_token.check_token(user, token):      ######################################
        user.verified = True
        user.save()
        msg = 'Account verified! Go ahead and Log in'
        return render('index.html', {'success' : msg})  
    else:
        msg = 'Authentication Failed!'
        return render('sign_up.html', {'error' : msg})

def createuser(request):
    username = request.POST['username']
    password = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    name = request.POST['name']
    roll_no=request.POST['roll_no']
    
    # check if the both the passwords are same
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        msg = 'An account with the given Username/Email already exists'
        return render(request, 'sign_up.html', {'errors' : msg})
    
    elif password != password2:
        msg = "Passwords don't match"
        return render(request, 'sign_up.html', {'errors' : msg})
        
    elif password == password2:
        # Email verification
        new_user = User(username=username, password=password, name=name,
                        email=email ,roll_no=roll_no)
        send_activation_email(new_user, request)
        msg = 'Please check your inbox for the activation of account'
        return render(request, 'index.html', {'success' : msg})
    
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        # ToDo: if no match with uid
        if user.password == password:
            return render(request, 'home/')
        else:
            msg = 'Incorrect Password!'
            return render(request, 'index.html', {'error' : msg})
    else:
        msg = 'Email not registered. Try Signing up'
        return render(request, 'index.html', {'error' : msg} )