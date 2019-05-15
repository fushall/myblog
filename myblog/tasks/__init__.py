from celery import Celery
from celery.contrib.abortable import AbortableTask

app = Celery(__name__,
             broker='mongodb://localhost:27017/celery',
             backend='mongodb://localhost:27017/celery')


@app.task(bind=True, Base=AbortableTask)
def hello(self, a):
    print('ready')
    for i in a[10]:
        if self.is_aborted():
            return 'aborted'
        self.update_state(state='PROGRESS', meta={'progress': (i + 1) * 10})
    print('done')
    return 'OK'


def on_raw_message(body):
    print(body)


def main():
    r = hello.apply_async((list(range(10)),))
    print(r.get(on_message=on_raw_message, propagate=True))


if __name__ == '__main__':
    main()
