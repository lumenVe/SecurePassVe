from fastapi import APIRouter
from securepassve_backend.api.v1.schemas.system import MetaResponse
from securepassve_backend.core.config import APP_NAME, ENV, VERSION

router = APIRouter()


@router.get("/meta", tags=["system"], response_model=MetaResponse)
def meta():
    return {"name": APP_NAME, "env": ENV, "version": VERSION}
