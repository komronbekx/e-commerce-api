from typing import TypedDict


class RegisterRequestDTO(TypedDict):
    email: str
    first_name: str
    last_name: str
    password: str
