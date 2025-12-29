from fastapi import APIRouter

from securepassve_backend.api.v1.schemas.vault import VaultStatusResponse
from securepassve_backend.api.v1.schemas.errors import ErrorResponse

router = APIRouter()

@router.get("/vault/status", tags=["vault"], response_model=VaultStatusResponse)
def vault_status():
    return {"exists": True}