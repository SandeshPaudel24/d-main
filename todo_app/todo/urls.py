from django.urls import path
from todo.views import *

urlpatterns = [
    path("", homepage),
    path("submit", submit, name="submit"),
    path("delete/<int:todo_id>", delete, name="delete_todo"),
]
