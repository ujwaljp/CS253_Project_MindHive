
from django.urls import path
from . import views

urlpatterns = [
    # eg: /users/1/
    path('', views.profile, name='view_user'),
     # eg: /users/1/edit/
    path('<int:user_id>/edit', views.edit, name='edit_users'),
]