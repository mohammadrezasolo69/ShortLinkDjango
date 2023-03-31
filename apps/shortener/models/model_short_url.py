from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count, Prefetch
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site

from apps.utils.models import DateBasic, StatusBasic
from apps.shortener.utils import generate_short_url
from apps.shortener.models.model_category import Category

from apps.shortener.validator import NoAspacesAllowed


class Shortener(DateBasic, StatusBasic):
    class Meta:
        verbose_name = _('Shortener')
        verbose_name_plural = _('Shortener')

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'),
                             related_name='shortener')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE,
                                 related_name='shortener', blank=True, null=True)
    long_url = models.URLField(_('Long URL'))
    short = models.CharField(_('Short'), validators=[NoAspacesAllowed], max_length=50, blank=True, null=True,
                             unique=True)
    password = models.CharField(_('Password'), max_length=15, blank=True, null=True)  # TODO:add validator
    expired_at = models.DateTimeField(_('Expired Time'), blank=True, null=True)
    QR_code = models.ImageField(_('QR Code'), blank=True, null=True, upload_to='shortener/short_urls/QR')

    def __str__(self):
        return self.short

    def save(self, *args, **kwargs):
        if not self.short:
            self.short = generate_short_url(length=10)

        if not self.check_expired_at:
            self.status = 'IA'

        super().save(*args, **kwargs)

    @property
    def get_expired_at(self):
        return self.expired_at.strftime('%H:%M - %Y/%m/%d')

    @property
    def get_short_url(self):
        return f"https://{Site.objects.get_current().domain}/{self.short}"

    @property
    def set_password(self):
        if self.password:
            return True
        return False

    @property
    def set_QR_code(self):
        if self.QR_code:
            return True
        return False

    @property
    def check_expired_at(self):
        if self.expired_at:
            if self.expired_at >= timezone.now():
                return True
            return False
        return 'not set'

    @property
    def set_expired_at(self):
        if not self.expired_at:
            return 'not set'
        return self.get_expired_at

    # @property
    # def get_count_click(self):
    #     query = Shortener.objects.select_related('category', 'user').get(pk=self.pk)
    #     return query.statistics.count()

    @property
    def get_count_click(self):
        query = Shortener.objects.only('id').get(id=self.pk)
        print(query)
        return query.statistics.count()

