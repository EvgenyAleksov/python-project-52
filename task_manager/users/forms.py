from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import CharField
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User


class UserForm(UserCreationForm):

    first_name = CharField(
        max_length=150,
        required=True,
        label=_("First name"))

    last_name = CharField(
        max_length=150,
        required=True,
        label=_("Last name"))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2'
        )


class UserUpdateForm(UserChangeForm):
    password = None

    password1 = CharField(
        label=_("Password"),
        strip=False)

    password2 = CharField(
        label=_("Password confirmation"),
        strip=False,
        help_text=_("Enter the same password as before, for verification."))

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2'
        )
