from apps.core.exceptions import DomainError
from rest_framework import status


class InvalidToken(DomainError):
    http_status = status.HTTP_401_UNAUTHORIZED
    code: str = "invalid_token"
    title: str = "Invalid Token"
