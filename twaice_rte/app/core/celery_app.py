from concurrent.futures import ThreadPoolExecutor
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


@celery.task
def calculate_metrics(df_json: dict[str, Any], nominal_capacity: float) -> Metric:
    """
    Calculates the RTE and C-rate of a battery from given data.
    Uses a ThreadPoolExecutor to calculate the metrics in parallel.

    Args:
        df_json (dict[str, Any]): JSON representation of the data.
        nominal_capacity (float): Nominal capacity of the battery in Ah.

    Returns:
        Metric: The calculated metrics.

    """

    df = pd.DataFrame.from_dict(df_json)

    with ThreadPoolExecutor() as executor:
        rte_future = executor.submit(rte, df)
        c_rate_future = executor.submit(c_rate, df, nominal_capacity)

        result = Metric(
            rte=rte_future.result(),
            c_rate=c_rate_future.result(),
            total_data_points=len(df),
        )
    return result
