from typing import Literal

from fastapi import APIRouter

from twaice_rte.app.api.v1 import metrics

router = APIRouter(prefix="/v1")


@router.get("/")  # Add the healthcheck endpoint
def status() -> Literal["OK"]:
    return "OK"


router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
