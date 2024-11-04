from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User


class TestUsers(TestCase):

    def test_create_user(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create.html')

        response = self.client.post(
            reverse('user_create'),
            {
                'first_name': 'T1',
                'last_name': 'M1',
                'username': 'TM1',
                'password1': 'TM111111',
                'password2': 'TM111111',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        user = User.objects.last()
        self.assertEqual(user.first_name, 'T1')
        self.assertEqual(user.last_name, 'M1')
        self.assertEqual(user.username, 'TM1')

        response = self.client.get(reverse('users'))
        self.assertTrue(len(response.context['users']) == 1)

    def test_update_user(self):
        user = User.objects.get(id=8)

        response = self.client.get(
            reverse('user_update', kwargs={'pk': user.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        self.client.force_login(user)
        response = self.client.get(
            reverse('user_update', kwargs={'pk': user.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/users.html')
        response = self.client.post(
            reverse('user_update', kwargs={'pk': user.id}),
            {
                'first_name': 'T1',
                'last_name': 'M1',
                'username': 'TM1',
                'password1': 'TM111111',
                'password2': 'TM111111',
            }
        )
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'T1')

    def test_DeleteUser(self):
        user = User.objects.get(username='TM1')

        response = self.client.get(
            reverse('user_delete', kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        self.client.force_login(user)
        response = self.client.get(
            reverse('user_delete', kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('user_delete', kwargs={'pk': user.id})
        )
        self.assertRedirects(response, reverse('users'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
