from apps.auth.services.auth import AuthService
from apps.auth.services.me import MeService
from apps.auth.validators import CompositePasswordValidator, MinLengthValidator, SpecialCharacterValidator
from apps.users.container import get_user_service


def get_auth_service() -> AuthService:
    password_validator = CompositePasswordValidator([
        MinLengthValidator(),
        SpecialCharacterValidator(),
    ])
    return AuthService(
        user_service=get_user_service(),
        password_validator=password_validator,
    )


def get_me_service() -> MeService:
    return MeService(user_service=get_user_service())
