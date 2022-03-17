from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.view, name='view_home'),
    path('questions', views.allQuestionsView, name='view_questions'),
    path('search_results', views.search_results, name='search_results'),
    path('bookmarks', views.bookView, name='bookmarks'),
    path('following', views.folView, name='following'),
]
