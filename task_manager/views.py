from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .mixins import ProjectRedirectURLMixin

from django.http import HttpResponse


def index(request):
    a = None
    a.hello()  # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(ProjectRedirectURLMixin, LoginView):
    template_name = 'create.html'
    extra_context = {
        'title': 'Вход',
        'button_text': 'Войти'
    }
    next_page = reverse_lazy('index')
    success_message = 'Вы вошли в систему'


class LogoutUser(ProjectRedirectURLMixin, LogoutView):
    next_page = reverse_lazy('index')
    info_message = 'Вы вышли из системы'
