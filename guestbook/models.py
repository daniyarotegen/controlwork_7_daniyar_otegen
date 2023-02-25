from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    BLOCKED = 'BLOCKED', 'Blocked'


class Record(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(
        max_length=20, choices=StatusChoice.choices, default=StatusChoice.ACTIVE, verbose_name='Status'
    )

    def __str__(self):
        return self.name
