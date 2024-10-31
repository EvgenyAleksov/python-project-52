from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField

from task_manager.users.models import User


class UserForm(UserCreationForm):
    first_name = CharField(max_length=150,
                           required=True,
                           label='Имя')

    last_name = CharField(max_length=150,
                          required=True,
                          label='Фамилия')

    username = CharField(max_length=150,
                         required=True,
                         label='Имя пользователя',
                         help_text='Обязательное поле. Не более 150 символов.\
                         Только буквы, цифры и символы @/./+/-/_.')

    password1 = CharField(required=True,
                          label='Пароль',
                          help_text='* Ваш пароль должен содержать как минимум\
                          3 символа.')

    password2 = CharField(required=True,
                          label='Подтверждение пароля',
                          help_text='Для подтверждения введите, пожалуйста,\
                          пароль ещё раз.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2'
        )
