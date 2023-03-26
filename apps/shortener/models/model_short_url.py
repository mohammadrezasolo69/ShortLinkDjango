from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from qrcode.compat.pil import Image

from apps.utils.models import DateBasic, StatusBasic
from apps.shortener.utils import generate_short_url, generate_QR_code


class Shortener(DateBasic, StatusBasic):
    class Meta:
        verbose_name = _('Shortener')
        verbose_name_plural = _('Shortener')

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'),
                             related_name='shortener')
    long_url = models.URLField(_('Long URL'))
    short = models.CharField(_('Short'), max_length=50, blank=True, null=True, unique=True)
    password = models.CharField(_('Password'), max_length=15, blank=True, null=True)  # TODO:add validator
    expired_at = models.DateTimeField(_('Expired Time'), blank=True, null=True)
    QR_code = models.ImageField(_('QR Code'), blank=True, null=True, upload_to='shortener/short_urls/QR')

    # TODO:add category fields

    def __str__(self):
        return self.short

    def save(self, *args, **kwargs):
        if self.short in None:
            self.short = generate_short_url(length=10)
        super().save(*args, **kwargs)

    def get_expired_at(self):
        return self.expired_at.strftime('%H:%M - %Y/%m/%d')

    def get_short_url(self):
        return f"https://{Site.objects.get_current().domain}/{self.short}"
