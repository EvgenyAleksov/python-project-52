from django import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .mixins import ProjectRedirectURLMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль")


class LoginUser(ProjectRedirectURLMixin, LoginView):
    template_name = 'create.html'
    form_class = LoginForm
    extra_context = {
        'title': 'Вход',
        'button_text': 'Войти',
    }
    next_page = reverse_lazy('index')
    success_message = 'Вы залогинены'


class LogoutUser(ProjectRedirectURLMixin, LogoutView):
    next_page = reverse_lazy('index')
    info_message = 'Вы разлогинены'
