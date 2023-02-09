import uvicorn

# settings = get_settings()


def dev() -> None:
    """Run the uvicorn server in development environment."""
    uvicorn.run(
        "twaice_rte.app.main:app",  # path to the FastAPI application
        host="0.0.0.0",
        port=8000,
        # reload=settings.DEBUG,
    )
