from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.dto import UserDTO
from apps.users.services import UserService

from ..dto import LoginRequestDTO, LoginResponseDTO, RegisterRequestDTO, LogoutRequestDTO
from ..dto.register import RegisterResponseDTO
from ..exceptions.invalid_credentials import InvalidCredentials
from ..exceptions.invalid_token import InvalidToken
from ..exceptions.is_user_already_exists import IsUserAlreadyExists
from ..exceptions.weak_password import WeakPassword
from ..validators import CompositePasswordValidator, PasswordError


class AuthService:
    def __init__(
        self, user_service: UserService, password_validator: CompositePasswordValidator
    ) -> None:
        self.user_service = user_service
        self.password_validator = password_validator

    def register_email(self, dto: RegisterRequestDTO) -> RegisterResponseDTO:
        is_exists: bool = self.user_service.is_user_exists(dto["email"])

        if is_exists:
            raise IsUserAlreadyExists(dto["email"])

        try:
            self.password_validator.validate(dto["password"])
        except PasswordError:
            raise WeakPassword()

        new_user = self.user_service.create_user(dto)

        refresh = RefreshToken.for_user(new_user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return RegisterResponseDTO(
            access_token=access_token,
            refresh_token=refresh_token,
            user=UserDTO(
                id=new_user.id,
                email=new_user.email,
                first_name=new_user.first_name,
                last_name=new_user.last_name,
            ),
        )

    def login_email(self, dto: LoginRequestDTO) -> LoginResponseDTO:
        user = self.user_service.get_user_by_email(dto["email"])
        if not user or not user.check_password(dto["password"]):
            raise InvalidCredentials()

        user_data = UserDTO(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return LoginResponseDTO(
            access_token=access_token, refresh_token=refresh_token, user=user_data
        )

    def logout(self, dto: LogoutRequestDTO) -> None:
        try:
            token = RefreshToken(dto["refresh_token"])  # type: ignore[arg-type]
            token.blacklist()
        except TokenError:
            raise InvalidToken("Invalid or expired refresh token")
