from typing import Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[int]
    username: str
    password: str
    first_name: str
    last_name: str
    is_staff: bool
    is_active: bool
