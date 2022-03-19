from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view_question, name='view_question'),
    path('<int:question_id>/edit', views.edit_question, name='edit_question'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('follow-bookmark', views.follow_bookmark, name='follow_bookmark'),
    path('<int:question_id>/report', views.report, name='report'),
    path('<int:question_id>/add-comment', views.add_comment, name='add_comment'),
    path('<int:question_id>/add-answer', views.add_answer, name='add_answer'),
    # eg: /questions/askform/
    path('askform/', views.QuestionCreateView.as_view(),name="add_question"),
]
