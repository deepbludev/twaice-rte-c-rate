from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from twaice_rte.app import api

app = FastAPI(
    title="Twaice RTE",
    description="Base project for FastAPI",
    default_response_class=ORJSONResponse,
)


# Add the router responsible for all /api/ endpoint requests
app.include_router(api.router)
