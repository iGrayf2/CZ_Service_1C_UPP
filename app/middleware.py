import logging
import time
from collections.abc import Awaitable, Callable

from fastapi import Request, Response

logger = logging.getLogger("cz_service.http")


async def log_http_requests(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    start_time = time.perf_counter()

    body = await request.body()
    body_text = body.decode("utf-8", errors="replace") if body else ""

    logger.info(
        "REQUEST %s %s from=%s body=%s",
        request.method,
        request.url.path,
        request.client.host if request.client else "unknown",
        body_text,
    )

    response = await call_next(request)

    duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
    logger.info(
        "RESPONSE %s %s status=%s duration_ms=%s",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )

    return response
