from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView

from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.filters import TaskFilter
from task_manager.users.models import User

from task_manager.mixins import (ProjectLoginRequiredMixin,
                                 HasPermissionTaskDeleteMixin)


class TaskListView(FilterView,
                   ListView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {'button_text': 'Показать'}


class TaskCreateView(ProjectLoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create.html'
    success_url = reverse_lazy('task_list')
    success_message = ('Задача успешно создана')
    extra_context = {
        'title': 'Задачи',
        'button_text': 'Создать задачу',
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(ProjectLoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'create.html'
    success_url = reverse_lazy('task_list')
    success_message = 'Задача успешно изменена'
    extra_context = {
        'title': 'Изменение задачи',
        'button_text': 'Изменить',
    }


class TaskDeleteView(ProjectLoginRequiredMixin,
                     SuccessMessageMixin,
                     HasPermissionTaskDeleteMixin,
                     DeleteView):
    model = Task
    template_name = 'delete.html'
    extra_context = {
        'title': 'Удаление задачи',
        'button_text': 'Да, удалить',
    }
    success_url = reverse_lazy('task_list')
    success_message = 'Задача успешно удалена'
    denied_url = reverse_lazy('task_list')
    permission_denied_message = 'Задачу может удалить только ее автор'


class TaskView(ProjectLoginRequiredMixin,
               DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        task = self.get_object()
        context = super().get_context_data(**kwargs)
        context['name'] = task.name
        return context
