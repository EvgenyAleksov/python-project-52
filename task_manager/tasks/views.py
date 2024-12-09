from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from task_manager.mixins import (
    HasPermissionTaskDeleteMixin,
    ProjectLoginRequiredMixin,
)
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskListView(FilterView, ListView):

    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {'button_text': _('Show')}


class TaskCreateView(ProjectLoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')
    success_message = _('Task is successfully created')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(ProjectLoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task_list')
    success_message = _('Task is successfully updated')


class TaskDeleteView(ProjectLoginRequiredMixin,
                     SuccessMessageMixin,
                     HasPermissionTaskDeleteMixin,
                     DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = _('Task is successfully deleted')
    denied_url = reverse_lazy('task_list')
    permission_denied_message = _('The task can be deleted only by its author')


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
