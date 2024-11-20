from django import forms
from django.forms import ModelForm, CharField

from task_manager.users.models import User
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskForm(ModelForm):
    name = CharField(label='Имя')

    description = CharField(label='Описание')

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}))

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
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
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Имя',
        #             'class': 'form-control'
        #         }
        #     ),
        #     'description': forms.Textarea(
        #         attrs={
        #             'placeholder': 'Описание',
        #             'cols': 40,
        #             'rows': 10,
        #             'class': 'form-control'
        #         }
        #     )
        # }
        # labels = {
        #     'name': 'Имя',
        #     'description': 'Описание'
        # }
