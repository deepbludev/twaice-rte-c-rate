from typing import Literal

import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel

from twaice_rte.libs import metrics

app = FastAPI(
    title="Twaice RTE",
    description="Base project for FastAPI",
    default_response_class=ORJSONResponse,
)


# Add the router responsible for all /api/ endpoint requests
# app.include_router(api.router)


@app.get("/")  # Add the healthcheck endpoint
def status() -> Literal["OK!"]:
    return "OK!"


class RTEResponse(BaseModel):
    rte: float
    c_rate: float
    total_data_points: int


@app.post("/rte")
def rte(data: UploadFile = File(...)) -> RTEResponse:
    df = pd.read_csv(data.file)
    return RTEResponse(
        rte=metrics.rte(df),
        c_rate=metrics.c_rate(df, 100),
        total_data_points=len(df),
    )
