from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
    )

    description = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name=_('Description')
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
    )

    labels = models.ManyToManyField(
        Label,
        through='TaskLabelRelationships',
        through_fields=('task', 'label'),
        blank=True,
        related_name='labels'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class TaskLabelRelationships(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
