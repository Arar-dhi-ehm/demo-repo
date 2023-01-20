from django.urls import path

from . import views  # The '.' means import views from the current directories

# Define paths to different webpages 
urlpatterns = [
    path('', views.index, name='index'),  # If path is null, user will be directed to views.py
    path('view_1/', views.view_1, name='view-1'),
]