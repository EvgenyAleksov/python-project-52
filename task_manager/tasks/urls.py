from django.urls import path

from task_manager.tasks.views import (TaskListView, TaskCreateView,
                                      TaskUpdateView, TaskDeleteView,
                                      TaskView)

urlpatterns = [

    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/', TaskView.as_view(), name='task')
]
