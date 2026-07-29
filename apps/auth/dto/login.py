from typing import TypedDict

from apps.users.dto import UserDTO


class LoginRequestDTO(TypedDict):
    email: str
    password: str


class LoginResponseDTO(TypedDict):
    access_token: str
    refresh_token: str
    user: UserDTO
