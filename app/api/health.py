from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/ping")
def ping() -> dict[str, str | bool]:
    return {
        "ok": True,
        "service": "CZ_Service_1C_UPP",
        "message": "Связь с сервисом работает",
    }
