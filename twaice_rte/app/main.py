from typing import Literal

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    title="Twaice RTE",
    description="Base project for FastAPI",
    default_response_class=ORJSONResponse,
)


# Add the router responsible for all /api/ endpoint requests
# app.include_router(api.router)


@app.get("/")  # Add the healthcheck endpoint
def status() -> Literal["OK"]:
    return "OK"
