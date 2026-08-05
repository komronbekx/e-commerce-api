from apps.core.exceptions import DomainError
from rest_framework import status


class EmptyCart(DomainError):
    http_status = status.HTTP_400_BAD_REQUEST
    code: str = "empty_cart"
    title: str = "Empty Cart"
