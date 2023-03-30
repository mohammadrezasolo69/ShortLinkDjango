import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def IpChecker(value):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    if re.search(pattern, value):
        raise ValidationError(_('The entered IP is not valid'))
