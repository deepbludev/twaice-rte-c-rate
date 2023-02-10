import pandas as pd
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, PositiveFloat

from twaice_rte.app.core.celery_app import calculate_metrics
from twaice_rte.app.models.metrics import Metric

# from twaice_rte.app.worker import calculate_metrics

router = APIRouter()


class TriggerCalculateMetricsResponse(BaseModel):
    """Response model for the calculate_metrics endpoint.

    Attributes:
        task_id (str): ID of the task that calculates the metrics for later retrieval.
    """

    task_id: str


@router.post(
    "/",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=TriggerCalculateMetricsResponse,
)
def trigger_calculate_metrics(
    nominal_capacity: PositiveFloat = Form(
        description="Nominal capacity of the battery in Ah",
    ),
    data: UploadFile = File(description="CSV file containg datapoints"),
) -> TriggerCalculateMetricsResponse:
    """Triggers the calculation of the RTE and C-rate of a battery from given data."""

    try:
        df = pd.read_csv(data.file)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Problem reading csv file: {str(e)}"
        )

    task = calculate_metrics.apply_async(args=[df.to_dict(), nominal_capacity])
    return TriggerCalculateMetricsResponse(task_id=task.id)


class GetMetricsResponse(BaseModel):
    """Response model for the get_metrics endpoint."""

    state: str
    data: Metric | None


@router.get("/{task_id}")
async def get_metrics(task_id: str) -> GetMetricsResponse:
    try:
        task = calculate_metrics.AsyncResult(task_id)
        return GetMetricsResponse(state=task.state, data=task.result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
