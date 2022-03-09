from django.urls import path

from . import views

url_patterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view, name='view_question'),
    # eg: /questions/ask/
    path('ask/', views.ask, name='ask_question'),
]