from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create a function that will create a multiple views. This will serve the http requests. 
def index(response, name):
    # Get an item in todolist using ID
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1 )
    # Create a header or text for webpage
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, str(item.text))) # %s will get the value of %ls.name