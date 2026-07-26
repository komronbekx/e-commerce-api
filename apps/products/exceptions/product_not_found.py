from rest_framework.status import HTTP_404_NOT_FOUND
from apps.core.exceptions.domain_error import DomainError


class ProductNotFound(DomainError):
    http_status = HTTP_404_NOT_FOUND
    code = "product_not_found"
    title = "Product Not Found"
