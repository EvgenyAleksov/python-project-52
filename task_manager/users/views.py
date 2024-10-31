from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.users.forms import UserForm


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'create.html'
    success_url = reverse_lazy('login')
    success_message = ('Пользователь успешно зарегистрирован')
    extra_context = {
        'title': ('Регистрация'),
        'button_text': ('Зарегистрировать'),
    }
