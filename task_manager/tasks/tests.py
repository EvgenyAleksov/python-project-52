from django.test import TestCase
from django.urls import reverse

from task_manager.tasks.models import Task
from task_manager.users.models import User


class TestTasks(TestCase):
    fixtures = ['users.json',
                'statuses.json',
                'labels.json',
                'tasks.json']

    def test_task_list(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        response = self.client.get(reverse('task_list'))
        self.assertTrue(len(response.context['tasks']), 2)

    def test_task_create(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create.html')

        response = self.client.post(reverse('task_create'), {
            'name': 't3',
            'description': 'd3',
            'status': 1,
            'author': 1,
            'executor': 1})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))

        response = self.client.get(reverse('task_list'))
        self.assertTrue(len(response.context['tasks']), 3)

    def test_task_update(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        task = Task.objects.get(id=1)

        response = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}),
            {
                'name': 't111',
                'description': 'd111',
                'status': 1,
                'author': 1,
                'executor': 1,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        task.refresh_from_db()
        self.assertEqual([task.name, task.description], ['t111', 'd111'])

    def test_task_delete(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        response = self.client.post(reverse('task_delete',
                                    kwargs={'pk': 2}))
        self.assertRedirects(response, reverse('task_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(pk=1).name, 't1')
