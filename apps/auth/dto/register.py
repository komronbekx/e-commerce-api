from typing import TypedDict

from apps.users.dto import UserDTO


class RegisterRequestDTO(TypedDict):
    email: str
    first_name: str
    last_name: str
    password: str


class RegisterResponseDTO(TypedDict):
    access_token: str
    refresh_token: str
    user: UserDTO
