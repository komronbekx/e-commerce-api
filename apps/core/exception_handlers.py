from rest_framework.response import Response
from rest_framework.views import exception_handler
from apps.core.exceptions.domain_error import DomainError


def custom_exception_handler(exc: Exception, context: dict) -> Response | None:
    if isinstance(exc, DomainError):
        return Response(
            {
                "code": exc.code,
                "title": exc.title,
                "detail": exc.detail,
            },
            status=exc.http_status,
        )
    return exception_handler(exc, context)
