# MindHive URL Configuration
# The `urlpatterns` list routes URLs to views.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


# urlpatterns to match the urls with the views
urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),          # index page
    path('admin/', admin.site.urls),                           # admin page
    path('questions/', include('questions.urls',
         namespace='questions')),                              # questions app urls
    path('users/', include('users.urls', namespace='users')),  # users app urls
    path('home/', include('home.urls', namespace='home'))      # home app urls
]

# add the media files to the urlpatterns
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
