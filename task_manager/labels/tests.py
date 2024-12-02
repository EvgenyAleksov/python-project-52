from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User
from task_manager.labels.models import Label


class TestLabels(TestCase):


    def setUp(self):
        User.objects.create(
            first_name='T1',
            last_name='M1',
            username='TM1',
        )
        self.user = User.objects.get(id=1)
        Label.objects.create(name='label1')
        Label.objects.create(name='label2')
        Label.objects.create(name='label3')

    def test_label_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('label_list'))
        self.assertTrue(len(response.context['labels']), 3)

    def test_label_create(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('label_create'),
                                    {'name': 'label4'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('label_list'))

        response = self.client.get(reverse('label_list'))
        self.assertTrue(len(response.context['labels']), 4)

    def test_label_update(self):
        self.client.force_login(self.user)
        label = Label.objects.get(id=1)

        response = self.client.post(reverse('label_update',
                                    kwargs={'pk': 1}),
                                    {'name': 'label111'})
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, 'label111')

    def test_label_delete(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('label_delete',
                                    kwargs={'pk': 3}))
        self.assertRedirects(response, reverse('label_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 2)
        self.assertEqual(Label.objects.get(pk=1).name, 'label1')
        self.assertEqual(Label.objects.get(pk=2).name, 'label2')
