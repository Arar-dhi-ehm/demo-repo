from django.urls import path

from . import views  # The '.' means import views from the current directories

# Define paths to different webpages 
urlpatterns = [
    path('<str:name>', views.index, name='index'),  # If path is null, user will be directed to views.py
    # '<int:id>' means look for some integer in the path and pass it to function views.index
]
