from typing import Any

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/test", tags=["test"])


@router.post("/echo")
def echo(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": True,
        "received": payload,
    }
