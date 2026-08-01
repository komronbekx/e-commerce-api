from typing import TypedDict


class LogoutRequestDTO(TypedDict):
    refresh_token: str
