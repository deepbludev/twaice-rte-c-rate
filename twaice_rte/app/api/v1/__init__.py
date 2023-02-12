from fastapi import APIRouter

from twaice_rte.app.api.v1.endpoints import metrics
from twaice_rte.app.core.config import get_settings

settings = get_settings()
router = APIRouter(prefix=f"/{settings.API_V1_STR}")


router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
