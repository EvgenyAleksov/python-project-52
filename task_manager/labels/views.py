from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager.mixins import (ProjectLoginRequiredMixin,
                                 EntityProtectedMixin)


class LabelListView(ListView):

    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class LabelCreateView(ProjectLoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'create.html'
    success_url = reverse_lazy('label_list')
    success_message = _('Label is successfully created')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(ProjectLoginRequiredMixin,
                      SuccessMessageMixin,
                      UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'create.html'
    success_url = reverse_lazy('label_list')
    success_message = _('Label is successfully updated')
    extra_context = {
        'title': _('Update label'),
        'button_text': _('Update'),
    }


class LabelDeleteView(ProjectLoginRequiredMixin,
                      SuccessMessageMixin,
                      EntityProtectedMixin,
                      DeleteView):
    model = Label
    template_name = 'delete.html'
    extra_context = {
        'title': _('Delete label'),
        'button_text': _('Yes, delete'),
    }
    success_url = reverse_lazy('label_list')
    success_message = _('Label is successfully deleted')
    denied_url = reverse_lazy('label_list')
    protected_message = _('Unable to delete a label because it is being used')
