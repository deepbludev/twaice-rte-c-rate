from typing import Any

import pandas as pd
from celery import Celery

from twaice_rte.app.models.metrics import Metric
from twaice_rte.libs.metrics import c_rate, rte

celery = Celery(
    "worker",
    broker="amqp://guest:guest@localhost:5672",
    backend="db+sqlite:///db.sqlite3",
)


# celery.conf.task_routes = {"twaice_rte.app.worker": "main-queue"}


@celery.task
def calculate_metrics(df_json: dict[str, Any], nominal_capacity: float) -> Metric:
    df = pd.DataFrame.from_dict(df_json)

    result = Metric(
        rte=rte(df),
        c_rate=c_rate(df, nominal_capacity),
        total_data_points=len(df),
    )
    return result
