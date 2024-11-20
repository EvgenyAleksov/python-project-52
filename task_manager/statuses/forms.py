from django.forms import ModelForm, CharField

from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    name = CharField(label='Имя')

    class Meta:
        model = Status
        fields = ['name']
