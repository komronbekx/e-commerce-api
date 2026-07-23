from rest_framework import status
from .domain_error import DomainError


class CategoryNotFound(DomainError):
    http_status = status.HTTP_404_NOT_FOUND
    code: str = "category_not_found"
    title: str = "Category Not Found"
