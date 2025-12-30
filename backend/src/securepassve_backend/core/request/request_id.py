from __future__ import annotations

import time
import uuid
from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from securepassve_backend.core.request.request_context import request_id_ctx


class RequestIDMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger, header_name: str = "X-Request-ID"):
        super().__init__(app)
        self.logger = logger
        self.header_name = header_name

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start = time.perf_counter()

        incoming = request.headers.get(self.header_name)
        request_id = incoming.strip() if incoming else str(uuid.uuid4())
        
        token = request_id_ctx.set(request_id)
        try:
            response = await call_next(request)
        except Exception as e:
            duration_ms = (time.perf_counter() - start) * 1000
            self.logger.exception(
                "request_error",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "duration_ms": round(duration_ms, 2),
                    "error": str(e),
                },
            )
            raise
        finally:
            request_id_ctx.reset(token)

        duration_ms = (time.perf_counter() - start) * 1000

        response.headers[self.header_name] = request_id

        self.logger.info(
            "request_completed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": round(duration_ms, 2),
            },
        )

        return response