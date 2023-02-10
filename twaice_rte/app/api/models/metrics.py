from pydantic import BaseModel


class Metric(BaseModel):
    """Model for the metrics.

    Attributes:
        rte (float): Roundtrip efficiency of the battery.
        c_rate (float): C-rate of the battery.
        total_data_points (int): Number of data points in the input file.
    """

    rte: float
    c_rate: float
    total_data_points: int
