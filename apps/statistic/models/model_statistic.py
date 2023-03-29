from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shortener.models import Shortener


class Statistic(models.Model):
    class Meta:
        verbose_name = _('Statistic')
        verbose_name_plural = _('Statistics')
        ordering = ('-time_click',)

    ip = models.CharField(_('IP'), max_length=45, primary_key=True)
    os = models.CharField(_('os'), max_length=200)
    time_click = models.DateTimeField(_('time click'), auto_now_add=True)
    browser = models.CharField(_('Browser'), max_length=200)
    country = models.CharField(_('Country'), max_length=200)
    language = models.CharField(_('Language'), max_length=200)
    shortener = models.ForeignKey(Shortener, on_delete=models.CASCADE, related_name='statistics',
                                  verbose_name=_('Shortener'))

    def __str__(self):
        return self.ip

    @property
    def get_time_click(self):
        return self.time_click.strftime('%H:%M - %Y/%m/%d')
