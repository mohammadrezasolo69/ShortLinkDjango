

from .base import *


LOCAL_APPS = [
    "django_seed",
    "debug_toolbar",
]

MIDDLEWARE += "debug_toolbar.middleware.DebugToolbarMiddleware",

INSTALLED_APPS += LOCAL_APPS

INTERNAL_IPS = [
    '127.0.0.1',
]
