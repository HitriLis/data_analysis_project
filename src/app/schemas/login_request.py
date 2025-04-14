from pydantic import BaseModel
from datetime import datetime


class LoginRequest(BaseModel):
    GUID: str
    Timestamp: datetime
    OuterIP: str
    NgToken: str


class LoginResponse(BaseModel):
    new_ip: bool
    new_token: bool
