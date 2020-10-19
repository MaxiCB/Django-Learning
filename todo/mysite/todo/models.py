from django.db import models


class Todo(models.Model):
    todo_name = models.CharField(max_length=50)
    todo_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')
    todo_open = models.BooleanField(default=True)
    def __str__(self):
        return self.todo_name

class Task(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=200)
    task_complete = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date added')
    def __str__(self):
        return self.task_description
