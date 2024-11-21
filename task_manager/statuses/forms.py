from django import forms
from django.forms import ModelForm, CharField

from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    name = CharField(label='Имя')

    class Meta:
        model = Status
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                  'class': 'form-control'})}
