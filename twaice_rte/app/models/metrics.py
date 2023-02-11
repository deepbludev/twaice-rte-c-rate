from pydantic import BaseModel, Field


class Metric(BaseModel):
    """Model for the metrics.

    Attributes:
        rte (float): Roundtrip efficiency of the battery.
        c_rate (float): C-rate of the battery.
        total_data_points (int): Number of data points in the input file.
    """

    rte: float = Field(
        description="Roundtrip efficiency of the battery.",
        gt=0,
        lt=1,
    )
    c_rate: float = Field(
        description="C-rate of the battery.",
        gt=0,
        lt=1,
    )
    total_data_points: int = Field(
        description="Number of data points in the input file.",
        gt=0,
    )
