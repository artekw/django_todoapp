from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone

class TaskCategory(models.Model):
    category_name = models.CharField(
        max_length=50, verbose_name=_('Kategoria'))

    def __str__(self):
        return self.category_name

class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Nazwa zdarzenia'))
    category = models.ForeignKey(
        TaskCategory, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Kategoria'))
    description = models.TextField(
        max_length=100, blank=True, verbose_name=_('Opis zdarzenia'))
    created_date = models.DateTimeField(
        default=timezone.now, blank=True, null=True, verbose_name=_('Data dodania zdarzenia'))
    task_date = models.DateTimeField(
        blank=True, null=True, verbose_name=_('Początek trwania zdarzenia'))
    task_deadline = models.DateTimeField(
        blank=True, null=True, verbose_name=_('Planowany termin zakończenia zdarzenia'))
    task_done = models.BooleanField(
        default=False, verbose_name=_('Data zakończenia zdarzenia'))
    task_important = models.BooleanField(
        default=False, verbose_name=_('Pilne!'))
    gcal_id = models.TextField(
        max_length=50, blank=True, verbose_name=_('Google Calendar ID'))

    def __str__(self):
        return self.name
