"""MindHive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('questions/', include('questions.urls')),
    path('users/', include('users.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sign_up/', views.signup, name='signup'),
<<<<<<< HEAD
    path('sign_up/createuser', views.createuser, name='createuser'),
    path('sign_up/otp', views.otp, name='otp'),
    # path('verify/<uid_b64e>/<token>', views.activate_account, name='activate')
=======
    path('sign_up/createuser', views.createuser, name='createuser')
>>>>>>> 84eb2fee38ebdaf40507cb3b6aedba1c16ba204c
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)