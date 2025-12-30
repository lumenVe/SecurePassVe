# Sentinel V1.2 Logging System

import json
import logging
import os
import sys
from datetime import datetime, timezone

from securepassve_backend.core.request_context import request_id_ctx

class RequestIDFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        rid = request_id_ctx.get()
        if rid and not hasattr(record, "request_id"):
            record.request_id = rid
        return True


class SentinelJsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "file": record.filename,
            "line": record.lineno,
            "function": record.funcName,
        }

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)

        reserved = {
            "name", "msg", "args", "levelname", "levelno",
            "pathname", "filename", "module",
            "exc_info", "exc_text", "stack_info",
            "lineno", "funcName",
            "created", "msecs", "relativeCreated",
            "thread", "threadName",
            "processName", "process", "taskName"
        }

        for key, value in record.__dict__.items():
            if key in reserved:
                continue
            if key.startswith("_"):
                continue
            if key in payload:
                continue
            payload[key] = value

        return json.dumps(payload, ensure_ascii=False)


def configure_sentinel_logging() -> None:
    level_name = os.getenv("SECUREPASSVE_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    root = logging.getLogger()
    root.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(SentinelJsonFormatter())
    handler.addFilter(RequestIDFilter())

    # wichtig: keine Doppel-Logs bei reload
    root.handlers.clear()
    root.addHandler(handler)

    logging.getLogger("uvicorn").setLevel(level)
    logging.getLogger("uvicorn.error").setLevel(level)
    logging.getLogger("uvicorn.access").setLevel(level)
