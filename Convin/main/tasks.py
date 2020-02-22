from celery import Celery, task
from celery.decorators import periodic_task
from datetime import timedelta
from celery.schedules import crontab
from django.conf import settings
import main


app = Celery('main', broker='amqp://localhost', backend='amqp://localhost', include=['Convin.tasks'])


@app.task
def daily_alert():

    print('\nSendind Daily Alerts....')
    # send_mail('Daily Alert!',
    # task_desc,
    # 'your_email@host.com',
    # email)
    for obj in main.models.TaskTracker.objects.all():
        if obj.update_type.casefold()=="daily":
            print('Daily Alert: '+obj.task.task_desc)

@app.task
def weekly_alert():
    print('\nSending Weekly Alerts....')

    for obj in main.models.TaskTracker.objects.all():
        if obj.update_type.casefold()=="weekly":
                # send_mail('Weekly Alert!',
                # task_desc,
                # 'your_email@host.com',
                # recepient.email)
            print('Weekly Alert:\t'+ obj.task.task_desc)

@app.task
def monthly_alert():
    print('\nSending Monthly Alerts....')

    for obj in main.models.TaskTracker.objects.all():
        if obj.update_type.casefold()=="monthly":
                # send_mail('Monthly Alert!',
                # task_desc,
                # 'your_email@host.com',
                # recepient.email)
            print('Sending to: '+obj.email)
            print('Monthly Alert:\t'+ obj.task.task_desc)
