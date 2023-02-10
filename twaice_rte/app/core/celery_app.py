from celery import Celery

celery = Celery(
    "worker",
    broker="amqp://guest:guest@localhost:5672",
    backend="db+sqlite:///db.sqlite3",
)


# celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
