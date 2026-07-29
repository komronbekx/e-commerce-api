import uuid
from typing import TypedDict


class UserDTO(TypedDict):
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    is_active: bool
