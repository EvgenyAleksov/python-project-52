from django.contrib import messages
from django.contrib.auth.views import RedirectURLMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin


class ProjectRedirectURLMixin(RedirectURLMixin):
    next_page = None
    success_message = None
    info_message = None

    def get_default_redirect_url(self):
        if self.next_page:
            if self.success_message:
                messages.success(self.request, self.success_message)
            elif self.info_message:
                messages.info(self.request, self.info_message)
        return super().get_default_redirect_url()


class ProjectLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    denied_message = 'Вы не авторизованы! Пожалуйста, выполните вход.'

    def handle_no_permission(self):
        messages.error(self.request, self.denied_message)
        return redirect(self.login_url)


class ProjectUserPassesTestMixin(UserPassesTestMixin):
    denied_url = None
    permission_denied_message = None

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.denied_url)
        return super().dispatch(request, *args, **kwargs)


class HasPermissionUserChangeMixin(ProjectUserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user


class HasPermissionTaskDeleteMixin(ProjectUserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user


class ProjectFormMixin(FormMixin):
    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['name'] = object.name
        return context
