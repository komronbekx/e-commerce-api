from apps.core.exceptions import DomainError
from rest_framework import status


class CartItemNotFound(DomainError):
    http_status = status.HTTP_404_NOT_FOUND
    code: str = "cart_item_not_found"
    title: str = "CartItem Not Found"
