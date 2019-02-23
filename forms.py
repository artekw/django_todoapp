from django.utils.translation import gettext_lazy as _

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'category', 'description',
                  'task_date', 'task_important')
        labels = {
            'name': _('Nazwa zadania'),
            'category': _('Kategoria'),
            'description': _('Opis zadania'),
            'task_date': _('Termin zadania'),
            'task_important': _('Pilne!'),
        }
        widgets = {
            'task_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }


