from django.test import TestCase
from django.urls import reverse

# from task_manager.statuses.models import Status


class TestStatus(TestCase):

    def test_create_status(self):
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, template_name='create.html')
