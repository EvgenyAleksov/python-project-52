from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from task_manager.mixins import (ProjectLoginRequiredMixin,
                                 EntityProtectedMixin)


class StatusListView(ListView):

    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class StatusCreateView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully created')
    # extra_context = {
    #     'title': _('Create status'),
    #     'button_text': _('Create'),
    # }


class StatusUpdateView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_update.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully updated')
    # extra_context = {
    #     'title': _('Update status'),
    #     'button_text': _('Update'),
    # }


class StatusDeleteView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       EntityProtectedMixin,
                       DeleteView):
    model = Status
    template_name = 'delete.html'
    extra_context = {
        'title': _('Delete status'),
        'button_text': _('Yes, delete'),
    }
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully deleted')
    denied_url = reverse_lazy('status_list')
    protected_message = _('Unable to delete a status because it is being used')
