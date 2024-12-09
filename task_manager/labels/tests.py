from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.users.models import User


class TestLabels(TestCase):
    fixtures = ["labels.json", "users.json"]

    def test_label_list(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        response = self.client.get(reverse("label_list"))
        self.assertTrue(len(response.context["labels"]), 3)

    def test_label_create(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)

        response = self.client.post(reverse("label_create"), {"name": "l"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("label_list"))

        response = self.client.get(reverse("label_list"))
        self.assertTrue(len(response.context["labels"]), 4)

    def test_label_update(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)
        label = Label.objects.get(id=1)

        response = self.client.post(
            reverse("label_update", kwargs={"pk": 1}), {"name": "l111"}
        )
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, "l111")

    def test_label_delete(self):
        user = User.objects.get(username="TM1")
        self.client.force_login(user)

        response = self.client.post(reverse("label_delete", kwargs={"pk": 3}))
        self.assertRedirects(response, reverse("label_list"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 2)
        self.assertEqual(Label.objects.get(pk=1).name, "l1")
        self.assertEqual(Label.objects.get(pk=2).name, "l2")
