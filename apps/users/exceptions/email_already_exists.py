from apps.core.exceptions import DomainError


class EmailAlreadyExists(DomainError):
    http_status = 409
    code = "email_already_exists"
    title = "Email Already Exists"
