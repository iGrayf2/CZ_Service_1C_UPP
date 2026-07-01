from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.test import router as test_router

app = FastAPI(
    title="CZ Service 1C UPP",
    description="Сервис интеграции 1С УПП с Честным Знаком",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(test_router)
