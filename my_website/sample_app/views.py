from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from django.shortcuts import get_object_or_404

# Create a function that will create a multiple views. This will serve the http requests. 
def index(response, id):
    # Get an item in todolist using ID
    # ls = ToDoList.objects.get(id=id)
    ls = get_object_or_404(ToDoList, pk=1)
    # return render(response, 'my_website/list.html', {'ls':ls}) # The '{}' means open dictionary
    return render(response, "my_website/base.html", {"name": ls.name})

# Create a function for homepage in urls.py
def home(response):
    return render(response, 'my_website/home.html', {})