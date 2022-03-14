from django.urls import path

from . import views

urlpatterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view, name='view_question'),
    path('<int:question_id>/like', views.like, name='like_question'),
    path('<int:question_id>/dislike', views.dislike, name='dislike_question'),
    path('<int:question_id>/edit', views.edit, name='edit_question'),
    path('<int:question_id>/add-comment', views.add_comment, name='add_comment'),
    # eg: /questions/askform/
    path('<int:user_id>/askform', views.QuestionCreateView.as_view()),
]