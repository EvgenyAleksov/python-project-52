from django.views.generic import ListView

from task_manager.users.models import User


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
