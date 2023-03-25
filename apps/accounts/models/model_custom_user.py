from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.accounts.manager import CustomUserManager


class CustomUser(AbstractUser):
    """ Custom User class  """

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    username = None
    email = models.EmailField(_('email'), unique=True)
    avatar = models.ImageField(_('avatar'), upload_to='accounts/users/avatar', blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
