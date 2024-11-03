from celery import Celery

app = Celery('celery')
app.config_from_object('celeryconfig', namespace='CELERY')


@app.task
def add_numbers():
    return