from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


from apps.utils.models import DateBasic, StatusBasic


class Category(DateBasic, StatusBasic):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    title = models.CharField(_('title'), max_length=220)
    slug = models.SlugField(_('slug'), unique=True)
    color = ColorField(_('Color'),default='#32a852')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'),
                             related_name='categories')
