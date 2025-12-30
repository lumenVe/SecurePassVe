import logging
from fastapi import APIRouter, Depends


from securepassve_backend.api.v1.schemas.vault import VaultStatusResponse
from securepassve_backend.api.v1.schemas.errors import ErrorResponse
from securepassve_backend.vault.deps import get_vault_repository
from securepassve_backend.vault.repository import VaultRepository

log = logging.getLogger(__name__)

router = APIRouter()

@router.get("/vault/status", tags=["vault"], response_model=VaultStatusResponse)
def vault_status(userID: str, repository: VaultRepository = Depends(get_vault_repository)):
    exists = repository.vault_exists(userID)
    log.info("vault_status_checked", 
            extra={
                "user_id": userID,
                "exists": exists,
            },
    )
    return {"exists": exists}