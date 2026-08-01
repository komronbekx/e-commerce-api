import uuid

from apps.auth.dto import MeUpdateRequestDTO
from apps.users.models import User
from apps.users.services import UserService


class MeService:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def get_me(self, user_id: uuid.UUID) -> User:
        return self.user_service.get_user_by_id(user_id)

    def update_me(self, user_id: uuid.UUID, dto: MeUpdateRequestDTO) -> User:
        user = self.user_service.get_user_by_id(user_id)

        if "first_name" in dto:
            user.first_name = dto["first_name"]

        if "last_name" in dto:
            user.last_name = dto["last_name"]

        return self.user_service.update_user(user)
