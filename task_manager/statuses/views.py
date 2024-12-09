from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import EntityProtectedMixin, ProjectLoginRequiredMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


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


class StatusUpdateView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_update.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully updated')


class StatusDeleteView(ProjectLoginRequiredMixin,
                       SuccessMessageMixin,
                       EntityProtectedMixin,
                       DeleteView):
    model = Status
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully deleted')
    denied_url = reverse_lazy('status_list')
    protected_message = _('Unable to delete a status because it is being used')
