from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    # eg: /home/1/
    path('', views.view, name='view_home'),
    path('search_results', views.search_results, name='search_results'),
]
