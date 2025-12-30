from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError


from securepassve_backend.api.v1.router import router as v1_router
from securepassve_backend.core.exceptions import ApiError
from securepassve_backend.core.sentinel import configure_sentinel_logging

app = FastAPI(title="SecurePassVe API")

app.include_router(v1_router, prefix="/api/v1")

configure_sentinel_logging()

import logging
from securepassve_backend.core.request_id import RequestIDMiddleware
access_log = logging.getLogger("securepassve_backend.access")

app.add_middleware(RequestIDMiddleware, logger=access_log)

@app.exception_handler(ApiError)
async def api_error_handler(request: Request, exc: ApiError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.error, "message": exc.message},
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    error_map = {
        400: "bad_request",
        401: "unauthorized",
        403: "forbidden",
        404: "not_found",
        409: "conflict",
        422: "validation_error",
        429: "rate_limited",
        500: "internal_error",
    }
    error_code = error_map.get(exc.status_code, "http_error")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": error_code, "message": str(exc.detail)},
    )
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0] if exc.errors() else None
    if first_error:
        loc = " -> ".join(str(x) for x in first_error.get("loc", []))
        msg = first_error.get("msg", "Invalid request.")
        message = f"{loc}: {msg}" if loc else msg
    else:
        message = "Invalid request."

    return JSONResponse(
        status_code=422,
        content={"error": "validation_error", "message": message},
    )
