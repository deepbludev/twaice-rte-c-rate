from concurrent.futures import ThreadPoolExecutor
from typing import Any

import pandas as pd
from celery import Celery

from twaice_rte.app.models.metrics import Metric
from twaice_rte.libs.metrics import c_rate, rte

from .config import get_settings

settings = get_settings()

queue = Celery(
    "worker",
    broker=settings.BROKER_URL,
    backend=settings.TASK_DB_URL,
)


@queue.task
def calculate_metrics(data: dict[str, Any], nominal_capacity: float) -> Metric:
    """
    Calculates the RTE and C-rate of a battery from given data.
    Uses a ThreadPoolExecutor to calculate the metrics in parallel.

    Args:
        df_json (dict[str, Any]): JSON representation of the data.
        nominal_capacity (float): Nominal capacity of the battery in Ah.

    Returns:
        Metric: The calculated metrics.

    """

    df = pd.DataFrame.from_dict(data)

    with ThreadPoolExecutor() as executor:
        rte_future = executor.submit(rte, df)
        c_rate_future = executor.submit(c_rate, df, nominal_capacity)

        result = Metric(
            rte=rte_future.result(),
            c_rate=c_rate_future.result(),
            total_data_points=len(df),
        )
    return result
