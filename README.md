# SecurePassVe

SecurePassVe is a learning project where I build a password manager to practice full-stack development and security fundamentals.

Planned scope:
- Backend API (local first, later potentially deployable)
- Web frontend
- Encrypted vault storage with the goal of client-side encryption (the backend should store ciphertext only)

Disclaimer:
This project is under active development and is not intended for storing real passwords.

## Repository structure

- `backend/` — Python/FastAPI backend (current focus)
- `frontend/` — planned

## Run the backend locally (Windows / PowerShell)

Prerequisites:
- Python 3.12+
- Git

Steps:

```powershell
cd backend
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -U pip
pip install -e ".[dev]"
uvicorn securepassve_backend.main:app --reload
```

Then:
- Healthcheck: http://127.0.0.1:8000/health
- API docs: http://127.0.0.1:8000/docs

## License

MIT
