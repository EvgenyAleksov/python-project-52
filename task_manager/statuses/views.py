from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from task_manager.mixins import (ProjectLoginRequiredMixin)


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class StatusCreateView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'create.html'
    success_url = reverse_lazy('status_list')
    success_message = ('Статус успешно создан')
    extra_context = {
        'title': 'Создать статус',
        'button_text': 'Создать',
    }


class StatusUpdateView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'create.html'
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно изменен'
    extra_context = {
        'title': 'Изменение статуса',
        'button_text': 'Изменить',
    }


class StatusDeleteView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       DeleteView):
    model = Status
    template_name = 'delete.html'
    extra_context = {
        'title': 'Удаление статуса',
        'button_text': 'Да, удалить',
    }
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно удален'
    denied_url = reverse_lazy('status_list')
    permission_denied_message = 'У вас нет прав для изменения\
                                 другого пользователя.'
    protected_message = 'Невозможно удалить статус, потому что он используется'
