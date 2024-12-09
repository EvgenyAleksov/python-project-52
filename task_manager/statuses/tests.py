from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.users.models import User


class TestStatuses(TestCase):
    fixtures = ["statuses.json", "users.json"]

    def test_status_list(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        response = self.client.get(reverse("status_list"))
        self.assertTrue(len(response.context["statuses"]), 3)

    def test_status_create(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        response = self.client.post(
            reverse("status_create"), {"name": "s4"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("status_list"))

        response = self.client.get(reverse("status_list"))
        self.assertTrue(len(response.context["statuses"]), 4)

    def test_status_update(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        status = Status.objects.get(pk=1)

        response = self.client.post(
            reverse("status_update", kwargs={"pk": 1}), {"name": "s111"}
        )
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, "s111")

    def test_status_delete(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)

        response = self.client.post(reverse("status_delete", kwargs={"pk": 3}))
        self.assertRedirects(response, reverse("status_list"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.get(pk=1).name, "s1")
        self.assertEqual(Status.objects.get(pk=2).name, "s2")
