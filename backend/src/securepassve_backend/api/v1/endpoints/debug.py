from fastapi import APIRouter
from securepassve_backend.core.exceptions import ApiError
from securepassve_backend.api.v1.schemas.errors import ErrorResponse
from securepassve_backend.api.v1.schemas.debug import EchoResponse

router = APIRouter()


@router.get("/debug/error", tags=["debug"], responses={418: {"model": ErrorResponse}})
def raise_error():
    raise ApiError(error="demo_error", message="This is a demo error.", status_code=418)

@router.get("/debug/echo", tags=["debug"], response_model=EchoResponse, responses={422: {"model": ErrorResponse}})
def echo_times(times: int):
    return {"times": times}
