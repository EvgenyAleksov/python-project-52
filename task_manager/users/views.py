from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.users.forms import UserForm, UserUpdateForm
from task_manager.mixins import (ProjectLoginRequiredMixin,
                                 HasPermissionUserChangeMixin)


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        users = User.objects.exclude(username='Evgeny')
        return users


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'create.html'
    success_url = reverse_lazy('login')
    success_message = ('Пользователь успешно зарегистрирован')
    extra_context = {
        'title': 'Регистрация',
        'button_text': 'Зарегистрировать',
    }


class UserUpdateView(ProjectLoginRequiredMixin,
                     HasPermissionUserChangeMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'create.html'
    extra_context = {
        'title': 'Изменение пользователя',
        'button_text': 'Изменить',
    }
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно изменен'
    denied_url = reverse_lazy('users')
    permission_denied_message = 'У вас нет прав для изменения\
                                 другого пользователя.'


class UserDeleteView(ProjectLoginRequiredMixin,
                     HasPermissionUserChangeMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = User
    template_name = 'delete.html'
    extra_context = {
        'title': 'Удаление пользователя',
        'button_text': 'Да, удалить',
    }
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно удален'
    denied_url = reverse_lazy('users')
    permission_denied_message = 'У вас нет прав для изменения\
                                 другого пользователя.'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['name'] = user.first_name + user.last_name
        return context
