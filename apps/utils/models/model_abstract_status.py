from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusBasic(models.Model):
    class Meta:
        abstract = True

    status = models.BooleanField(_('Status'), default=True)
