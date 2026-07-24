from .services import CategoryService
from .repositories import CategoryRepository


def get_category_repository() -> CategoryRepository:
    return CategoryRepository()


def get_category_service() -> CategoryService:
    return CategoryService(repo=get_category_repository())
