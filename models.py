from django.db import models
from django.utils import timezone

class TaskCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        TaskCategory, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    task_date = models.DateTimeField(blank=True, null=True)
    task_done = models.BooleanField(default=False)
    task_important = models.BooleanField(default=False)

    def __str__(self):
        return self.name
