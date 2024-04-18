import os
from celery import Celery
from celery.schedules import crontab
from django.db.models.signals import post_save

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProject.settings')

app = Celery('NewsProject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_notifications_weekly': {
        'task': 'news.tasks.send_notifications_weekly',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
    },
}