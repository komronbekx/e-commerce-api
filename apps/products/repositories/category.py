from django.db.models import QuerySet
from ..models import Category
import uuid

class CategoryRepository:

    def get_all_categories(self) -> QuerySet[Category]:
        return Category.objects.all()

    def get_category_by_id(self, category_id: uuid.UUID) -> Category | None:
        return Category.objects.filter(id=category_id).first()

    def create(self, category: Category) -> Category:
        category.save()
        return category

    def update(self, category: Category) -> Category:
        category.save()
        return category

    def delete(self, category_id: uuid.UUID) -> None:
        Category.objects.filter(id=category_id).delete()
