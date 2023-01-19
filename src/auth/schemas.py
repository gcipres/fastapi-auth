from pydantic import BaseModel
from uuid import UUID

class UserSession(BaseModel):
    jwt: str
    id: UUID
    name: str
    email: str