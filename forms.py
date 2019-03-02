import datetime

from django.utils.translation import gettext_lazy as _

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'category', 'description',
                  'task_date', 'task_deadline', 'task_important')
        widgets = {
            'task_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'task_deadline': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }

    def event(self):
        event = {
            'summary': self.cleaned_data['name'],
            'description': self.cleaned_data['description'],
            'start': {
                'dateTime': self.cleaned_data['task_date'].isoformat(),
            },
            'end': {
                'dateTime': self.cleaned_data['task_deadline'].isoformat(),
            }
        }

        return event


