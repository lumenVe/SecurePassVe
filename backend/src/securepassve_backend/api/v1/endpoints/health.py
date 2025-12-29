from fastapi import APIRouter
from securepassve_backend.api.v1.schemas.system import HealthResponse

router = APIRouter()

@router.get("/health", status_code=200, tags=["system"], response_model=HealthResponse)
def health():
    return {"status": "ok"}