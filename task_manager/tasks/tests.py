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

        Task.objects.create(
            name='task1',
            description='d1',
            status_id=1,
            author_id=1,
            executor_id=1,
        )
        Task.objects.create(
            name='task2',
            description='d2',
            status_id=1,
            author_id=1,
            executor_id=1,
        )

    def test_task_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('task_list'))
        self.assertTrue(len(response.context['tasks']), 2)

    def test_task_create(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create.html')

        response = self.client.post(reverse('task_create'), {
            'name': 'task3',
            'description': 'd3',
            'status': 1,
            'author': 1,
            'executor': 1})

        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('task_list'))
        self.assertTrue(len(response.context['tasks']), 3)

    def test_task_update(self):
        self.client.force_login(self.user)
        task = Task.objects.get(id=1)

        response = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}),
            {
                'name': 'task111',
                'description': 'd111',
                'status': 1,
                'author': 1,
                'executor': 1,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        task.refresh_from_db()
        self.assertEqual([task.name, task.description], ['task111', 'd111'])

    def test_task_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('task_delete',
                                    kwargs={'pk': 2}))
        self.assertRedirects(response, reverse('task_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(pk=1).name, 'task1')
