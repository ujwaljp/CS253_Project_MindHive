from django.urls import path
from . import views

urlpatterns = [
    # eg: /home/1/
    path('<int:user_id>', views.view, name='view_home'),
    path('searchbar/', views.searchbar, name='searchbar'),
]