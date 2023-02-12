from typing import Literal

from fastapi import APIRouter

from twaice_rte.app.api import v1
from twaice_rte.app.core.config import get_settings

router = APIRouter(prefix="/api")
router.include_router(v1.router)


@router.get("/")
def healthcheck() -> Literal["OK"]:
    return "OK"


base_url = f"/api/{get_settings().API_V1_STR}"
