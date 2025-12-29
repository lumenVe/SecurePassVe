from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class MetaResponse(BaseModel):
    name: str
    env: str
    version: str
