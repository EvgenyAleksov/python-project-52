from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User


class TestUsers(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='T1',
            last_name='M1',
            username='TM1',
        )
        User.objects.create(
            first_name='T2',
            last_name='M2',
            username='TM2',
        )

    def test_user_list(self):
        response = self.client.get(reverse('users'))
        self.assertTrue(len(response.context['users']), 2)

    def test_user_create(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create.html')

        response = self.client.post(reverse('user_create'), {
                'first_name': 'T3',
                'last_name': 'M3',
                'username': 'TM3',
                'password1': 'TM333333',
                'password2': 'TM333333'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        user = User.objects.last()
        self.assertEqual(user.first_name, 'T3')
        self.assertEqual(user.last_name, 'M3')
        self.assertEqual(user.username, 'TM3')

        response = self.client.get(reverse('users'))
        self.assertTrue(len(response.context['users']), 3)

    def test_user_update(self):
        user = User.objects.get(id=2)

        response = self.client.get(reverse('user_update',
                                   kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        self.client.force_login(user)
        response = self.client.get(reverse('user_update',
                                   kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create.html')
        response = self.client.post(reverse('user_update',
                                    kwargs={'pk': user.id}), {
                'first_name': 'T222',
                'last_name': 'M222',
                'username': 'TM222',
                'password1': 'TM222222',
                'password2': 'TM222222'})
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'T222')

    def test_user_delete(self):
        user = User.objects.get(username='TM2')
        response = self.client.get(reverse('user_delete',
                                   kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        self.client.force_login(user)
        response = self.client.get(reverse('user_delete',
                                   kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('user_delete',
                                    kwargs={'pk': user.id}))
        self.assertRedirects(response, reverse('users'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
