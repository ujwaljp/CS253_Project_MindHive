
from django.urls import path
from .views import UserEditView
from . import views
urlpatterns = [
    # eg: /users/1/
    path('<int:pk>', views.profile, name='view_user'),
     # eg: /users/1/edit/
    path('<int:pk>/edit', UserEditView.as_view(), name='edit_users'),
]