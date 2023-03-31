import os
from celery import Celery

from core.settings import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.conf.update(
    result_backend=env('CELERY_BROKER_URL'),
    timezone='UTC',
    task_serializer='json',
)

app.autodiscover_tasks()
