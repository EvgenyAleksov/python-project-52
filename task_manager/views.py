from django import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .mixins import ProjectRedirectURLMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'create.html'
    form_class = LoginForm
    extra_context = {
        'title': 'Вход',
        'button_text': 'Войти',
    }
    next_page = reverse_lazy('index')
    success_message = 'Вы залогинены'

    def form_invalid(self, form):
        form.errors.clear()
        messages.error(
            self.request,
            "Пожалуйста, введите правильные имя пользователя и пароль. "
            "Оба поля могут быть чувствительны к регистру.")
        return super().form_invalid(form)


class LogoutUser(ProjectRedirectURLMixin, LogoutView):
    next_page = reverse_lazy('index')
    info_message = 'Вы разлогинены'
