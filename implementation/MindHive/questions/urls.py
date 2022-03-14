from django.urls import path

from . import views

urlpatterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view, name='view_question'),
    # eg: /questions/1/like/
    path('<int:question_id>/like/', views.like, name='like_question'),
    # eg: /questions/1/dislike/
    path('<int:question_id>/dislike/', views.dislike, name='dislike_question'),
    # eg: /questions/1/edit/
    path('<int:question_id>/edit/', views.edit, name='edit_question'),
    # eg: /questions/ask/
    path('<int:user_id>/askform', views.QuestionCreateView.as_view()),
]