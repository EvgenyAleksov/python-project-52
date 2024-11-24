from django import forms
from django.forms import ModelForm, CharField

from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskForm(ModelForm):
    name = CharField(label='Имя')

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        empty_label='---------',
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}))

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label='---------',
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-control'}))

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label='Метки',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False)

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')
        labels = {'description': 'Описание'}
