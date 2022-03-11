from django.shortcuts import render
from django.http import HttpResponse
from ..users.models import User
# Create your views here.
def view(request,user_id):
    usr = User.objects.get(id=user_id)
    return render(request, 'home/home.html', {'user': usr})