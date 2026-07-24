class DomainError(Exception):
    http_status: int = 400
    code: str = "domain_error"
    title: str = "Domain Error"
    detail: str = ""

    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail if detail is not None else self.title
        super().__init__(self.detail)
