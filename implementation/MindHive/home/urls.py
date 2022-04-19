from django.urls import path
from . import views


# define the namespace for the below urls
app_name='home'

urlpatterns = [
    path('', views.view, name='view_home'),                              # home page
    path('questions', views.allQuestionsView, name='view_questions'),    # all questions page
    path('search_results', views.search_results, name='search_results'), # search results page
    path('following/', views.folView, name='following'),                 # following page
    path('bookmarks/', views.bookView, name='bookmarks'),                # bookmarks page
    path('tags/<tagname>', views.tagView, name='tags'),                  # tag questions page
    path('authorQuestions', views.autQues, name='authorQuestions'),         # author questions page
    path('<int:user_id>/questions', views.otautQues, name='otherauthorQuestions') ,      # author questions page
]
