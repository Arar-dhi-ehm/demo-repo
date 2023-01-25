from django.urls import path
from . import views  # From the Project Root import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='index'),
    path('<str:pk>', views.go, name='go')
]