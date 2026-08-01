import uuid
from ..exceptions.email_already_exists import EmailAlreadyExists
from ..exceptions.user_not_found import UserNotFound
from ..models import User
from ..repositories import UserRepository
from ...auth.dto.register import RegisterRequestDTO


class UserService:

    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def create_user(self, dto: RegisterRequestDTO) -> User:
        if self.repo.exists_email(dto["email"]):
            raise EmailAlreadyExists(f"User with email {dto['email']} already exists")

        user = User(
            email=dto["email"],
            first_name=dto["first_name"],
            last_name=dto["last_name"],
            is_active=True,
            is_staff=False,
        )
        user.set_password(dto["password"])
        return self.repo.create(user)

    def update_user(self, user: User) -> User:
        return self.repo.update(user)

    def delete_user(self, user_id: uuid.UUID) -> None:
        if not self.repo.delete(user_id):
            raise UserNotFound(f"User with id {user_id} was not found")

    def get_user_by_id(self, user_id: uuid.UUID) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise UserNotFound(f"User with id {user_id} was not found")
        return user

    def get_user_by_email(self, email: str) -> User:
        user = self.repo.get_by_email(email=email)
        if not user:
            raise UserNotFound(f"User with email {email} was not found")
        return user

    def is_user_exists(self, email: str) -> bool:
        return self.repo.exists_email(email=email)
