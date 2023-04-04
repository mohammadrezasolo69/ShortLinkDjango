from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from core.settings import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core', broker='redis://')

# app.config_from_object('django.conf:settings')
app.conf.update(
    broker_url=env('CELERY_BROKER_URL'),
    timezone='UTC',
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    imports=['apps.statistic.tasks.save_statistic_task']
)

app.autodiscover_tasks()


