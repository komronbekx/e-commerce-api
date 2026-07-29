from apps.core.exceptions import DomainError


class UserNotFound(DomainError):
    http_status = 404
    title = "User Not Found"
    code = "user_not_found"
