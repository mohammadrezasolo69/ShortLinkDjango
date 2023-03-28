from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusBasic(models.Model):
    class Meta:
        abstract = True

    class StatusChooses(models.TextChoices):
        Active = 'AC'
        Inactive = 'IA'

    status = models.CharField(_('Status'), max_length=2, default=StatusChooses.Active, choices=StatusChooses.choices)
