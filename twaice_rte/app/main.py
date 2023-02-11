from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from twaice_rte.app import api

app = FastAPI(
    title="Twaice RTE Metrics",
    description="API for calculating the RTE and C-rate of a battery.",
    default_response_class=ORJSONResponse,
)

app.include_router(api.router)
