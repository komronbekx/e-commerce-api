import uuid
from django.db.models.query import QuerySet
from ..models import User


class UserRepository:
    def create(self, user: User) -> User:
        user.save()
        return user

    def update(self, user: User) -> User:
        user.save()
        return user

    def delete(self, user_id: uuid.UUID) -> bool:
        deleted_count, _ = User.objects.filter(id=user_id).delete()
        return deleted_count > 0

    def list(self) -> QuerySet[User]:
        return User.objects.all()

    def get_by_id(self, user_id: uuid.UUID) -> User | None:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> User | None:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def exists_email(self, email: str) -> bool:
        return User.objects.filter(email=email).exists()
