from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    # eg: /home/1/
    path('', views.view, name='view_home'),
<<<<<<< HEAD
    path('search_results', views.search_results, name='search_results'),
=======
    path('bookmarks/', views.bookView, name='bookmarks'),
    path('following/', views.folView, name='following'),
    path('searchbar/', views.searchbar, name='searchbar'),
>>>>>>> 3ae204d9051ff8ab2e785a179968653e5fb58b24
]
