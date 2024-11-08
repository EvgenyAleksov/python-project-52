from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

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
    success_message = ('Метка успешно создана')
    extra_context = {
        'title': 'Создать метку',
        'button_text': 'Создать',
    }


class LabelUpdateView(ProjectLoginRequiredMixin,
                      SuccessMessageMixin,
                      UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'create.html'
    success_url = reverse_lazy('label_list')
    success_message = 'Метка успешно изменена'
    extra_context = {
        'title': 'Изменение метки',
        'button_text': 'Изменить',
    }


class LabelDeleteView(ProjectLoginRequiredMixin,
                      SuccessMessageMixin,
                      EntityProtectedMixin,
                      DeleteView):
    model = Label
    template_name = 'delete.html'
    extra_context = {
        'title': 'Удаление метки',
        'button_text': 'Да, удалить',
    }
    success_url = reverse_lazy('label_list')
    success_message = 'Метка успешно удалена'
    denied_url = reverse_lazy('label_list')
    protected_message = 'Невозможно удалить метку, \
    потому что она используется'
