from apps.core.exceptions import DomainError


class WeakPassword(DomainError):
    http_status = 400
    code = "WEAK_PASSWORD"
    title = "Weak password"
