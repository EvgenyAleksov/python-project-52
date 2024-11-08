from django.forms import CheckboxInput
from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter

from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(queryset=Status.objects.all(), label='Статус')
    executor = ModelChoiceFilter(queryset=User.objects.all(),
                                 label='Исполнитель')
    labels = ModelChoiceFilter(queryset=Label.objects.all(), label='Метка')

    self_tasks = BooleanFilter(
        label='Только свои задачи',
        widget=CheckboxInput,
        method='filter_own_tasks'
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor',  'labels']
