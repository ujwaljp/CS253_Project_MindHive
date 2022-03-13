## Login page for new/tokenless user ## 

import re
from django.shortcuts import redirect, render
from users.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.contrib.auth.models import AbstractUser
# from .utils import generate_token
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# from django.contrib.auth import login, logout
from random import randint
from django.core.signing import Signer

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

def send_activation_email(user, request, OTP):
    current_site = get_current_site(request)
    subject = "Account Confirmation Email" 
    body = render_to_string('Mindhive/activate.html',{
        'user':user,
        'domain': current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.id)),
        'token':OTP          #######################################
    })
    print('here')
    print(user.email)
    
    send_mail(subject=subject,message = body,
                 from_email=settings.EMAIL_FROM_USER,
                 recipient_list=[user.email], fail_silently=False)
    # email.send()
    print('here')
    return

# def otp(request, uid_b64e, token):
def otp(request):
    username = request.session['username']
    password = request.session['password']
    email = request.session['email']
    name = request.session['name']
    roll_no=request.session['roll_no']
    OTP = request.session['OTP']
    try:
        user = User(username=username, password=password, name=name,
                        email=email ,roll_no=roll_no)
        # ToDo: if no match with uid
    except Exception as e:
        user=None 
        
    signer = Signer(settings.SECRET_KEY)
    value = signer.unsign(request.session['value'])
    
    if user and value == str(OTP):      ######################################
        user.verified = True
        user.save()
        msg = 'Account verified! Go ahead and Log in'
        return redirect('', {'success' : msg})
    else:
        msg = 'Authentication Failed!'
        return render(request, 'sign_up.html', {'error' : msg})

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
        OTP = randint(10000000,99999999)
        # print(OTP)
        send_activation_email(new_user, request, OTP)
        print('sent')
        signer = Signer(settings.SECRET_KEY)
        value = signer.sign(OTP)
        msg = 'Please check your inbox for the OTP'
        request.session['username'] = username
        request.session['password'] = password
        request.session['email'] = email
        request.session['name'] = name
        request.session['roll_no'] = roll_no
        request.session['OTP'] = OTP
        request.session['value'] = value
        return render(request, 'Mindhive/otp.html', {'success' : msg, 'value': value})
    
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