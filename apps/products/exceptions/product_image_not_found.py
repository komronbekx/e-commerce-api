from apps.core.exceptions import DomainError
from rest_framework import status


class ProductImageNotFound(DomainError):
    http_status = status.HTTP_404_NOT_FOUND
    default_detail = "ProductImage not found."
    default_code = "product_image_not_found"
