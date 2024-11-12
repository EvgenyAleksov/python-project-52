from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User
from task_manager.statuses.models import Status


class TestStatuses(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='T1',
            last_name='M1',
            username='TM1',
        )
        self.user = User.objects.get(id=1)
        Status.objects.create(name='status1')
        Status.objects.create(name='status2')
        Status.objects.create(name='status3')

    def test_status_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('status_list'))
        self.assertTrue(len(response.context['statuses']), 3)

    def test_status_create(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('status_create'),
                                    {'name': 'status4'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('status_list'))

        response = self.client.get(reverse('status_list'))
        self.assertTrue(len(response.context['statuses']), 4)

    def test_user_update(self):
        self.client.force_login(self.user)
        status = Status.objects.get(pk=1)

        response = self.client.post(reverse('status_update',
                                    kwargs={'pk': 1}),
                                    {'name': 'status111'})
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'status111')

    def test_user_delete(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('status_delete',
                                    kwargs={'pk': 3}))
        self.assertRedirects(response, reverse('status_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.get(pk=1).name, 'status1')
        self.assertEqual(Status.objects.get(pk=2).name, 'status2')
