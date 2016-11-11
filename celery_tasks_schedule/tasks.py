from __future__ import absolute_import
from celery_tasks_schedule.celery_settings import app
from Utility import app_store_utility as app_utl
from models.db_models import MongoDBClient
db_utl = MongoDBClient()

'''
http://docs.celeryproject.org/en/latest/userguide/routing.html
http://docs.celeryproject.org/en/latest/configuration.html#std:setting-CELERY_CREATE_MISSING_QUEUES
http://celery.readthedocs.io/en/latest/userguide/routing.html#amqp-primer
https://github.com/rduplain/celery-simple-example
http://docs.celeryproject.org/en/latest/getting-started/next-steps.html#routing
http://stackoverflow.com/questions/10079816/route-celery-task-to-specific-queue
http://stackoverflow.com/questions/16962449/how-to-send-periodic-tasks-to-specific-queue-in-celery
http://stackoverflow.com/questions/23129967/django-celery-multiple-queues-on-localhost-routing-not-working
'''
@app.task
def xtv_single_day_schedule_runner():
    db_utl.retrieve_xtv_day_review_comments()

@app.task
def xtv_connect_single_day_schedule_runner():
    db_utl.retrieve_xtv_connect_day_review_comments()

@app.task
def xtv_x1_remote_single_day_schedule_runner():
    db_utl.retrieve_xtv_x1_remote_day_review_comments()

@app.task
def xtv_remote_single_day_schedule_runner():
    db_utl.retrieve_xtv_remote_day_review_comments()

@app.task
def xtv_home_single_day_schedule_runner():
    db_utl.retrieve_xtv_home_day_review_comments()
