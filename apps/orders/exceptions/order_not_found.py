from apps.core.exceptions import DomainError
from rest_framework import status


class OrderNotFound(DomainError):
    http_status = status.HTTP_404_NOT_FOUND
    code: str = "order_not_found"
    title: str = "Order Not Found"
