from django.shortcuts import render
from django.http import HttpResponse


# Create your views here. This will serve the http requests.

# Create a function that will create a multiple views
def index(response):
    # Create a header or text for webpage
    return HttpResponse('<h1>Hello World!</h1>')

def view_1(response):
    # Create a header or text for webpage
    return HttpResponse('<h1>View Number 1!</h1>')