from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab
from kombu import Exchange, Queue
#amqp://venkatesh:password-1@localhost/venkatesh_vhost
#http://stackoverflow.com/questions/22466696/celery-beat-schedule-multiple-tasks-under-same-time-interval-group
app = Celery('celery_tasks_schedule',
             broker='amqp://',
             backend='amqp://',
             include=['celery_tasks_schedule.tasks'])

app.conf.update(CELERY_ENABLE_UTC=True,
                CELERY_TIMEZONE='America/New_York',
                CELERY_CREATE_MISSING_QUEUES = True,
                CELERYD_CONCURRENCY = 5,
                CELERY_QUEUES = (
                  Queue('xtv_task', Exchange('xtv_task'), routing_key='xtv_task_route'),
                  Queue('xtv_connect_task', Exchange('xtv_connect_task'), routing_key='xtv_connect_task_route'),
                  Queue('xtv_x1_remote_task', Exchange('xtv_x1_remote_task'), routing_key='xtv_x1_remote_task_route'),
                  Queue('xtv_remote_task', Exchange('xtv_remote_task'), routing_key='xtv_remote_task_route'),
                  Queue('xtv_home_task', Exchange('xtv_home_task'), routing_key='xtv_home_task_route'),
                ),
                CELERY_ROUTES = {
                    'celery_tasks_schedule.tasks.xtv_single_day_schedule_runner': {
                        'queue': 'xtv_task',
                        'routing_key': 'xtv_task_route',
                    },
                    'celery_tasks_schedule.tasks.xtv_connect_single_day_schedule_runner': {
                                            'queue': 'xtv_connect_task',
                                            'routing_key': 'xtv_connect_task_route',
                     },
                    'celery_tasks_schedule.tasks.xtv_x1_remote_single_day_schedule_runner': {
                                                                'queue': 'xtv_x1_remote_task',
                                                                'routing_key': 'xtv_x1_remote_task_route',
                    },
                    'celery_tasks_schedule.tasks.xtv_remote_single_day_schedule_runner': {
                                   'queue': 'xtv_remote_task',
                                    'routing_key': 'xtv_remote_task_route',
                                                                                },
                    'celery_tasks_schedule.tasks.xtv_home_single_day_schedule_runner': {
                                    'queue': 'xtv_home_task',
                                    'routing_key': 'xtv_home_task_route',
                     },
                },
                CELERYBEAT_SCHEDULE={
                    'xtv_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_single_day_schedule_runner',
                        'schedule': crontab(minute='*/30'),
                        'args': (),
                        },
                    'xtv_connect_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_connect_single_day_schedule_runner',
                        'schedule': crontab(minute='*/30'),
                        'args': (),
                        },
                    'xtv_x1_remote_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_x1_remote_single_day_schedule_runner',
                        'schedule': crontab(minute='*/30'),
                        'args': (),
                        },
                    'xtv_remote_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_remote_single_day_schedule_runner',
                        'schedule': crontab(minute='*/30'),
                        'args': (),
                        },
                    'xtv_home_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_home_single_day_schedule_runner',
                        'schedule': crontab(minute='*/30'),
                        'args': (),
                        },
                },
                )

if __name__ == '__main__':
    app.start()

'''
from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab
from kombu import Exchange, Queue
#amqp://venkatesh:password-1@localhost/venkatesh_vhost
#http://stackoverflow.com/questions/22466696/celery-beat-schedule-multiple-tasks-under-same-time-interval-group
app = Celery('celery_tasks_schedule',
             broker='amqp://',
             backend='amqp://',
             include=['celery_tasks_schedule.tasks'])

app.conf.update(CELERY_ENABLE_UTC=True,
                CELERY_TIMEZONE='America/New_York',
                CELERY_CREATE_MISSING_QUEUES = True,
                CELERYD_CONCURRENCY = 5,
                CELERYBEAT_SCHEDULE={
                    'xtv_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_single_day_schedule_runner',
                        'schedule': crontab(minute='*/60'),
                        'args': (),
                        },
                    'xtv_connect_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_connect_single_day_schedule_runner',
                        'schedule': crontab(minute='*/60'),
                        'args': (),
                        },
                    'xtv_x1_remote_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_x1_remote_single_day_schedule_runner',
                        'schedule': crontab(minute='*/60'),
                        'args': (),
                        },
                    'xtv_remote_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_remote_single_day_schedule_runner',
                        'schedule': crontab(minute='*/60'),
                        'args': (),
                        },
                    'xtv_home_tasks_schedule': {
                        'task': 'celery_tasks_schedule.tasks.xtv_home_single_day_schedule_runner',
                        'schedule': crontab(minute='*/60'),
                        'args': (),
                        },
                },
                )

if __name__ == '__main__':
    app.start()
'''
