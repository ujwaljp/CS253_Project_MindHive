from django.urls import path

from . import views

urlpatterns = [
    path('', views.profileview, name='profile'),
]