from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TestTasks(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='T1',
            last_name='M1',
            username='TM1',
        )
        self.user = User.objects.get(id=1)

        Status.objects.create(name='status1')
        self.status = Status.objects.get(id=1)

        Task.objects.create(
            name='task1',
            status_id='1',
            author_id='1',
            executor_id='1',
        )
        Task.objects.create(
            name='task2',
            status_id='1',
            author_id='1',
            executor_id='1',
        )

    def test_task_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('task_list'))
        self.assertTrue(len(response.context['tasks']), 2)
