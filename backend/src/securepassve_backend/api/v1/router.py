from fastapi import APIRouter

from securepassve_backend.core.config import ENV
from securepassve_backend.api.v1.endpoints.health import router as health_router
from securepassve_backend.api.v1.endpoints.meta import router as meta_router
from securepassve_backend.api.v1.endpoints.debug import router as debug_router
from securepassve_backend.api.v1.endpoints.vault import router as vault_router

router = APIRouter()
router.include_router(health_router)
router.include_router(meta_router)
router.include_router(vault_router)

if ENV == "dev":
    router.include_router(debug_router)