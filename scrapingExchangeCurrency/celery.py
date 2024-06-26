from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.apps import apps

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapingExchangeCurrency.settings')

# Import the tasks module
from scraping import tasks

app = Celery('scrapingExchangeCurrency')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
# app.autodiscover_tasks(['scraping'])
app.autodiscover_tasks()


# # Define the Celery beat schedule
# app.conf.beat_schedule = {
#     "send-schedule-emails": {
#         "task": "scraping.tasks.send_schedule_emails",
#         "schedule": 10.0,  # Schedule in seconds, adjust as needed
#         # Example of using crontab for scheduling
#         # "schedule": crontab(minute="*/30"),
#     },
# }
#
# # Optional configuration settings
# app.conf.timezone = 'Asia/Riyadh'
# app.conf.task_track_started = True
# app.conf.task_time_limit = 30 * 60


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
