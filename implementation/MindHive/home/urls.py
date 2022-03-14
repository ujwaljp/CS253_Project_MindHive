from django.urls import path
from . import views

urlpatterns = [
    # eg: /home/1/
    path('<int:user_id>', views.view, name='view_home'),
    path('search_results/', views.search_results, name='searchbar'),
]