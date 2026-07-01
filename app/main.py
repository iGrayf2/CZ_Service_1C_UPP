from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.test import router as test_router
from app.logging_config import setup_logging
from app.middleware import log_http_requests

setup_logging()

app = FastAPI(
    title="CZ Service 1C UPP",
    description="Сервис интеграции 1С УПП с Честным Знаком",
    version="0.1.0",
)

app.middleware("http")(log_http_requests)

app.include_router(health_router)
app.include_router(test_router)
