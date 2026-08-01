from apps.users.repositories import UserRepository
from apps.users.services.user import UserService


def get_user_service() -> UserService:
    repo = UserRepository()
    service = UserService(repo)
    return service
