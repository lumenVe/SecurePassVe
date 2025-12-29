from pydantic import BaseModel

class EchoResponse(BaseModel):
    times: int