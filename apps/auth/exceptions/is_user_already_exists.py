class IsUserAlreadyExists(Exception):
    def __init__(self, identifier: str) -> None:
        super().__init__(f"User with identifier {identifier} already exists.")
