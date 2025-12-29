# SecurePassVe

SecurePassVe is a **learning project** to build a password manager from scratch, with a strong focus on **backend architecture**, **security fundamentals**, and a future **zero‑knowledge design**.

This project is **not production software**. The goal is understanding *how* things work, not shipping a finished product.

---

## Goals

- Learn backend development with FastAPI
- Understand security fundamentals (no custom crypto)
- Work towards a zero‑knowledge architecture
  - Client‑side encryption
  - Backend stores **ciphertext only**
  - Master password never leaves the client
- Clean structure, versioned API, and explicit error contracts

---

## Backend

### Tech stack

- Python **3.12+**
- FastAPI
- Uvicorn
- src‑layout
- Ruff (linting/formatting)
- pytest (introduced gradually)

---

## Setup

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies (editable + dev extras):

```bash
pip install -e ".[dev]"
```

---

## Environment variables

The backend reads configuration from environment variables.

Currently used:

- `SECUREPASSVE_ENV` – application environment (`dev` | `prod`)

Recommended local setup:

Create a local `.env` file in `backend/` (not committed):

```env
SECUREPASSVE_ENV=dev
```

Start the server with:

```bash
uvicorn securepassve_backend.main:app --reload --env-file .env
```

---

## API documentation

Interactive API docs are available at:

```
http://127.0.0.1:8000/docs
```

---

## License

MIT

