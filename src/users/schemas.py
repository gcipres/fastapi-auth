import uuid
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class User(BaseModel):
    id: UUID = uuid.uuid4()
    email: str
    name: str
    password: Optional[str]
    create_at: Optional[float]