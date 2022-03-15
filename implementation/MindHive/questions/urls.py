from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view_question, name='view_question'),
    path('<int:question_id>/edit', views.edit_question, name='edit_question'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:question_id>/follow-bookmark', views.follow_bookmark, name='follow_bookmark'),
    path('<int:question_id>/add-comment', views.add_comment, name='add_comment'),
    # eg: /questions/askform/
    path('<int:user_id>/askform', views.QuestionCreateView.as_view()),
]
