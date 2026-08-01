class InvalidToken(Exception):
    def __init__(self, message: str = "Invalid Token") -> None:
        super().__init__(message)
