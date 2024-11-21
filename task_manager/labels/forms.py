from django import forms
from django.forms import ModelForm, CharField

from task_manager.labels.models import Label


class LabelForm(ModelForm):
    name = CharField(label='Имя')

    class Meta:
        model = Label
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                  'class': 'form-control'})}
