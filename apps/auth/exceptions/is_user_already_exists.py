from apps.core.exceptions import DomainError
from rest_framework import status


class IsUserAlreadyExists(DomainError):
    http_status = status.HTTP_409_CONFLICT
    code: str = "user_already_exists"
    title: str = "User Already Exists"

    def __init__(self, identifier: str) -> None:
        super().__init__(f"User with identifier {identifier} already exists.")