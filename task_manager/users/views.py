from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import (
    EntityProtectedMixin,
    HasPermissionUserChangeMixin,
    ProjectLoginRequiredMixin,
)
from task_manager.users.forms import UserForm, UserUpdateForm
from task_manager.users.models import User


class UsersListView(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "users"

    def get_queryset(self):
        users = User.objects.exclude(username="Evgeny")
        return users


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "users/user_create.html"
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")


class UserUpdateView(
    ProjectLoginRequiredMixin,
    HasPermissionUserChangeMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserUpdateForm
    template_name = "users/user_update.html"
    success_url = reverse_lazy("users")
    success_message = _("User is successfully updated")
    denied_url = reverse_lazy("users")
    permission_denied_message = _("You have no rights to change another user.")


class UserDeleteView(
    ProjectLoginRequiredMixin,
    HasPermissionUserChangeMixin,
    SuccessMessageMixin,
    EntityProtectedMixin,
    DeleteView,
):
    model = User
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("users")
    success_message = _("User is successfully deleted")
    denied_url = reverse_lazy("users")
    permission_denied_message = _("You have no rights to change another user.")
    protected_message = _("Unable to delete a user because he is being used")

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context["name"] = user.first_name + user.last_name
        return context
