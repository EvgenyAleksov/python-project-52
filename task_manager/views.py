from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView

from .mixins import ProjectRedirectURLMixin


class IndexView(TemplateView):

    template_name = 'index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    # extra_context = {
    #     'title': _('Log In'),
    #     'button_text': _('Enter'),
    # }
    next_page = reverse_lazy('index')
    success_message = _('You are logged in')


class LogoutUser(ProjectRedirectURLMixin, LogoutView):
    next_page = reverse_lazy('index')
    info_message = _('You are logged out')
