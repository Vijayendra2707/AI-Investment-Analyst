from fastapi import FastAPI

from api.routers.health import router as health_router

app = FastAPI(
    title="AI Investment Analyst API",
    version="1.0.0",
)

app.include_router(health_router)