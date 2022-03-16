
from django.urls import path, include
from .views import UserEditView
from . import views
from django.contrib.auth import views as auth_views
# from django.conf.urls import re_path

app_name = 'users'

urlpatterns = [
    # eg: /users/1/
    path('', views.testview, name='testview'),
    # path('', include('django.contrib.auth.urls')) ,
    path('login/',
        auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
        name='logout'),
    path('signup/',
        views.SignUp.as_view(), name='signup'),
    path('<int:pk>', views.profile, name='view_user'),
    # url(r'password_reset/$',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',email_template_name='users/password_reset_email.html',success_url='users/password_reset_done/'), name='reset_password'),
    # url(r'password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html')),
    path(r'password_reset_confirm(<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html',success_url='/users/password_reset_complete/'), name='password_reset_confirm'),
    # url(r'password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html')),
    # path('reset_password/',
    #  auth_views.PasswordResetView.as_view(template_name="users/password_reset.html",
    #  email_template_name='users/password_reset_email.html'),
    #  name="reset_password"),
    #
    # path('reset_password/done/',
    #     auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),
    #     name="password_reset_done"),
    #
    # path('reset/<uidb64>/<token>/',
    #  auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),
    #  name="password_reset_confirm"),
    #
    # path('reset_password_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"),
    #     name="password_reset_complete"),

    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
    #      email_template_name = 'users/password_reset_email.html'),
    #     name='reset_password'),
    # path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'),
    # name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'),
    #     name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
    #     name='password_reset_complete'),
     # eg: /users/1/edit/
    path('edit/', UserEditView.as_view(), name='edit_users'),
    path('addtags/',views.addTagsView.as_view(), name='addtags'),
]
