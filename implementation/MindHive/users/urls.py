
from django.urls import path
from .views import UserEditView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # eg: /users/1/
    path('', views.testview, name='testview'),
    path('login/',
        auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
        name='logout'),
    path('signup/',
        views.SignUp.as_view(), name='signup'),
    path('<int:pk>', views.profile, name='view_user'),
     # eg: /users/1/edit/
    path('edit/', UserEditView.as_view(), name='edit_users'),
]
