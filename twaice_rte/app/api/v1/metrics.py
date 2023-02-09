import pandas as pd
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

from twaice_rte.libs import metrics

router = APIRouter()


class RTEResponse(BaseModel):
    rte: float
    c_rate: float
    total_data_points: int


@router.post("/rte")
def rte(data: UploadFile = File(...)) -> RTEResponse:
    df = pd.read_csv(data.file)
    return RTEResponse(
        rte=metrics.rte(df),
        c_rate=metrics.c_rate(df, 100),
        total_data_points=len(df),
    )
