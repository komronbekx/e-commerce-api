import uuid
from apps.products.models import Category
from django.db.models import QuerySet
from ..exceptions.category_not_found import CategoryNotFound
from ..repositories import CategoryRepository


class CategoryService:
    def __init__(self, repo: CategoryRepository) -> None:
        self.repo = repo

    def get_categories(self) -> QuerySet[Category]:
        return self.repo.get_all_categories()

    def get_category_by_id(self, category_id: uuid.UUID) -> Category:
        category = self.repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFound(f"Category with id {category_id} not found")
        return category

    def create_category(self, category: Category) -> Category:
        self.repo.create(category)
        return category

    def update_category(
        self, category_id: uuid.UUID, category_data: Category
    ) -> Category:
        category = self.repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFound(f"Category with id {category_id} not found")

        category.name = category_data.name
        category.slug = category_data.slug
        self.repo.update(category)
        return category

    def delete_category(self, category_id: uuid.UUID) -> None:
        category = self.repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFound(f"Category with id {category_id} not found")
        self.repo.delete(category_id)
