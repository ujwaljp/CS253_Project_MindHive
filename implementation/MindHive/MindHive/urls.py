# MindHive URL Configuration
# The `urlpatterns` list routes URLs to views.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('questions/', include('questions.urls',namespace='questions')),
    path('users/', include('users.urls', namespace='users')),
    path('home/', include('home.urls', namespace='home')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
