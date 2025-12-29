from pydantic import BaseModel

class VaultStatusResponse(BaseModel):
    exists: bool