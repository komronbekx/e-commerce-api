from apps.core.exceptions import DomainError
from rest_framework import status


class InvalidCredentials(DomainError):
    http_status = status.HTTP_401_UNAUTHORIZED
    code: str = "invalid_credentials"
    title: str = "Invalid Credentials"
