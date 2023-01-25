from django.contrib import admin
from .models import Url  # Url is the class function of models.py under shortener app

# Register your models here. This is for the admin web page
admin.site.register(Url)