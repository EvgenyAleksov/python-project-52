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
                'password1': 'TM022008',
                'password2': 'TM022008',
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
        user = User.objects.get(id=1)

        response = self.client.get(
            reverse('update_user', kwargs={'pk': user.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
