from django.views.generic import ListView

from task_manager.statuses.models import Status
# from task_manager.statuses.forms import StatusForm


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
