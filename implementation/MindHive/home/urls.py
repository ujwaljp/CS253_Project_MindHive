from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    # eg: /home/1/
    path('', views.view, name='view_home'),
    path('bookmarks/', views.bookView, name='bookmarks'),
    path('following/', views.folView, name='following'),
    path('searchbar/', views.searchbar, name='searchbar'),
]
