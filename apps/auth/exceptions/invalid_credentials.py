class InvalidCredentials(Exception):
    """Invalid credentials exception"""

    def __init__(self, message: str = "Invalid Credentials") -> None:
        super().__init__(message)
