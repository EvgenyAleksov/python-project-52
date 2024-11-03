from django.contrib import admin

from .forms import UserForm, UserUpdateForm
from .models import User


# @admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    add_form = UserForm
    form = UserUpdateForm
    model = User
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'username',
                    'created_at')
    search_fields = ['username']


admin.site.register(User)
