from django.db import models

# Create your models here. For modelling information in database
# Create a todo list
class ToDoList(models.Model):  # 'models.Model' means create a db object called 'ToDoList'
    name = models.CharField(max_length=200)  # class var 'name' is an attribute of 'ToDoList'. CharField is where we store data.

    # Define a string method to see what it actually look like when printed
    def __str__(self) -> str:
        return self.name

# Create a model that is part of the ToDoList
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # Use ForeignKey to define a ToDoList obj. when we create an item
    text = models.CharField(max_length=300)
    complete = models.BooleanField()  # Boolean field is used to know if user have completed the items in todolist or not

    def __str__(self) -> str:
        return self.text