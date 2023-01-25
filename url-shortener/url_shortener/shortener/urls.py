from django.urls import path
from . import views  # From the Project Root import views

urlpatterns = [
    path('', views.index, name='index')
]