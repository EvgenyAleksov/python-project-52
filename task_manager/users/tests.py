from django.test import TestCase
from django.urls import reverse

# from task_manager.users.models import User


class TestUsers(TestCase):

    def test_create_user(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create.html')
