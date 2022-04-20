# declare the various endpoints of users/
from django.urls import path, include
from .views import UserEditView
from . import views
from django.urls import re_path
from django.contrib.auth import views as auth_views
# from django.conf.urls import re_path

app_name = 'users'

urlpatterns = [
    # eg: /users/1/
    path('', views.testview, name='testview'),
    # path('', include('django.contrib.auth.urls')) ,
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',
        views.signup, name='signup'),
    path('<int:pk>', views.profile, name='view_user'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',email_template_name='users/password_reset_email.html',success_url='/users/password_reset_done/'), name='reset_password'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html')),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html',success_url='/users/password_reset_complete/'), name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html')),
    path('edit/', UserEditView.as_view(), name='edit_users'),
    path('addtags/',views.addTagsView.as_view(), name='addtags'),
    path('notifications/', views.notifs_display, name='notifs'),
    path('users/', views.users_list_view, name='users_list'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate')
]
