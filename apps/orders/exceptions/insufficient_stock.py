from apps.core.exceptions import DomainError
from rest_framework import status


class InsufficientStock(DomainError):
    http_status = status.HTTP_409_CONFLICT
    code: str = "insufficient_stock"
    title: str = "Insufficient Stock"
