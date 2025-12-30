# SecurePassVe

SecurePassVe is a **learning project** to build a password manager from scratch with a focus on full‑stack development and security fundamentals.

This is **not production software**. The goal is to learn best practices (no custom crypto) and to work towards a **zero‑knowledge** architecture:
- Client‑side encryption
- Backend stores **ciphertext only**
- Master password never leaves the client

---

## Current status (backend)

Backend is a versioned FastAPI API under **`/api/v1`** with:
- System endpoints:
  - `GET /api/v1/health`
  - `GET /api/v1/meta`
- Vault (starter):
  - `GET /api/v1/vault/status?userID=<int>` (currently backed by an in‑memory repository; returns `{"exists": false}` unless seeded)
- Unified error format:
  - `{"error": "<code>", "message": "<text>"}`
  - Custom handlers for:
    - HTTP errors (including 404)
    - Validation errors (422)
- Debug routes are included **only in dev** (`SECUREPASSVE_ENV=dev`)
  - `GET /api/v1/debug/echo`
  - `GET /api/v1/debug/error`
- **Sentinel v1** logging:
  - Structured JSON logs (timestamp, level, logger, file, line, function, plus `extra` fields)
  - Request correlation via `X-Request-ID` (middleware)
  - Access log event: `request_completed` with request_id, method, path, status_code, duration_ms

---

## Setup (Windows / PowerShell)

Create and activate a virtual environment inside `backend/`:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies (editable + dev extras):

```powershell
pip install -e ".[dev]"
```

---

## Run the backend

From `backend/`:

```powershell
uvicorn securepassve_backend.main:app --reload --env-file .env
```

API docs:
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

---

## Tests

Run tests from `backend/`:

```powershell
pytest -q tests
```

---

## Environment variables

- `SECUREPASSVE_ENV`
  - `dev` (default) enables debug routes
  - `prod` disables debug routes
- `SECUREPASSVE_LOG_LEVEL`
  - e.g. `DEBUG`, `INFO`, `WARNING`, `ERROR` (default: `INFO`)

---

## Notes

- Prefer structured logs via `extra={...}` for filterable fields.

---

## License

MIT
