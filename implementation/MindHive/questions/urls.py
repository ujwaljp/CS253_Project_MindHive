from django.urls import path

from . import views

# namespace for the app
app_name = 'questions'

urlpatterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view_question,
         name='view_question'),         # view a question
    path('<int:question_id>/edit', views.edit_question,
         name='edit_question'),    # edit a question
    path('askform/', views.QuestionCreateView.as_view(),
         name="add_question"),     # add a question
    # vote on a question/answer
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('follow-bookmark', views.follow_bookmark,
         name='follow_bookmark'),       # follow / bookmark
    # report a question / answer
    path('<int:question_id>/report', views.report, name='report'),
    path('<int:question_id>/add-comment', views.add_comment,
         name='add_comment'),  # add a comment to a question / answer
    path('<int:question_id>/add-answer', views.add_answer,
         name='add_answer'),    # add an answer to a question
]
