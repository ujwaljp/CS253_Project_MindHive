from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view(request):
    return HttpResponse("Home page")