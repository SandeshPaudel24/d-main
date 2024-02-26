from django.db import models


# Create your models here.\
class todos(models.Model):
    text_add = models.TextField(default="Type Todo List")
