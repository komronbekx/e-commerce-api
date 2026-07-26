from .services import CategoryService, ProductService
from .repositories import CategoryRepository, ProductRepository


def get_category_repository() -> CategoryRepository:
    return CategoryRepository()


def get_category_service() -> CategoryService:
    return CategoryService(repo=get_category_repository())


def get_product_repository() -> ProductRepository:
    return ProductRepository()


def get_product_service() -> ProductService:
    return ProductService(
        repo=get_product_repository(), category_service=get_category_service()
    )
