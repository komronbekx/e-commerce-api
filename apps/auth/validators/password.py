import re
from abc import ABC, abstractmethod


class PasswordError(Exception):
    pass


class PasswordValidator(ABC):
    @abstractmethod
    def validate(self, password: str) -> None: ...


class MinLengthValidator(PasswordValidator):
    def __init__(self, min_length: int = 12) -> None:
        self.min_length = min_length

    def validate(self, password: str) -> None:
        if len(password) < self.min_length:
            raise PasswordError(
                f"Password is too short, minimum length is {self.min_length} characters."
            )


class SpecialCharacterValidator(PasswordValidator):
    _pattern = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")

    def validate(self, password: str) -> None:
        if not self._pattern.search(password):
            raise PasswordError("Password must contain at least one special character.")


class CompositePasswordValidator(PasswordValidator):
    def __init__(self, validators: list[PasswordValidator]) -> None:
        self._validators = validators

    def validate(self, password: str) -> None:
        for validator in self._validators:
            validator.validate(password)
