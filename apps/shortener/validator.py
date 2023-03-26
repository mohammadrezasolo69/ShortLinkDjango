from re import compile
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError


def NoAspacesAllowed(value):
    regex = compile(r'\s')
    if regex.search(value):
        raise ValidationError(_('No spaces allowed.'))
