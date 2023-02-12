from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from twaice_rte.app import api
from twaice_rte.app.core import config

settings = config.get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    version=settings.PROJECT_VERSION,
    description="API for calculating the RTE and C-rate of a battery.",
    default_response_class=ORJSONResponse,
)

app.include_router(api.router)
