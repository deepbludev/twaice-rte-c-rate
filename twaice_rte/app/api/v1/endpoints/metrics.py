import pandas as pd
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, PositiveFloat

from twaice_rte.libs.metrics import c_rate, rte

router = APIRouter()


class CalculateMetricsResponse(BaseModel):
    """Response model for the calculate_metrics endpoint.

    Attributes:
        rte (float): Roundtrip efficiency of the battery.
        c_rate (float): C-rate of the battery.
        total_data_points (int): Number of data points in the input file.
    """

    rte: float
    c_rate: float
    total_data_points: int


@router.post(
    "/",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=CalculateMetricsResponse,
)
def calculate_metrics(
    nominal_capacity: PositiveFloat = Form(
        description="Nominal capacity of the battery in Ah",
    ),
    data: UploadFile = File(description="CSV file containg datapoints"),
) -> CalculateMetricsResponse:
    """Calculates the RTE and C-rate of a battery from given data."""

    try:
        df = pd.read_csv(data.file)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Problem reading csv file: {str(e)}"
        )

    return CalculateMetricsResponse(
        rte=rte(df),
        c_rate=c_rate(df, nominal_capacity),
        total_data_points=len(df),
    )
