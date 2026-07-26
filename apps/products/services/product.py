import uuid
from typing import ClassVar

from django.core.files import File
from django.db.models.query import QuerySet
from .category import CategoryService
from ..models import Product, ProductImage
from ..repositories import ProductRepository
from ..exceptions import ProductNotFound


class ProductService:
    def __init__(
        self,
        repo: ProductRepository,
        category_service: CategoryService,
    ) -> None:
        self.repo = repo
        self.category_service = category_service

    UPDATABLE_FIELDS: ClassVar = [
        "name",
        "slug",
        "category",
        "description",
        "price",
        "stock",
        "is_active",
    ]

    def get_products(self) -> QuerySet[Product]:
        return self.repo.get_all_products()

    def get_product(self, product_id: uuid.UUID) -> Product:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product with id {product_id} was not found.")
        return product

    def get_product_by_name(self, product_name: str) -> Product:
        product = self.repo.get_product_by_name(product_name)
        if not product:
            raise ProductNotFound(f"Product with name {product_name} was not found.")
        return product

    def filter_products_by_category(self, category_id: uuid.UUID) -> QuerySet[Product]:
        return self.repo.filter_by_category(category_id)

    def create_product(self, product_data: dict) -> Product:
        category = self.category_service.get_category_by_id(product_data["category_id"])

        product = Product(
            name=product_data["name"],
            slug=product_data["slug"],
            category=category,
            description=product_data["description"],
            price=product_data["price"],
            stock=product_data["stock"],
        )
        self.repo.create(product)
        return product

    def update_product(self, product_id: uuid.UUID, product_data: dict) -> Product:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product with id {product_id} was not found.")

        category = self.category_service.get_category_by_id(product_data["category_id"])
        product.category = category

        for field in self.UPDATABLE_FIELDS:
            setattr(product, field, product_data[field])

        self.repo.update(product)
        return product

    def delete_product(self, product_id: uuid.UUID) -> None:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product with id {product_id} was not found.")
        self.repo.delete(product_id)

    def add_product_image(
        self,
        product_id: uuid.UUID,
        image_file: File,
        is_primary: bool = False,
        order: int = 0,
    ) -> ProductImage:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product with id {product_id} was not found.")

        if is_primary:
            self.repo.clear_primary_image(product_id)

        return self.repo.add_image(product, image_file, is_primary, order)

    def delete_image(self, image_id: uuid.UUID) -> None:
        self.repo.delete_image(image_id)

    def get_product_images(self, product_id: uuid.UUID) -> QuerySet[ProductImage]:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFound(f"Product with id {product_id} was not found.")
        return self.repo.get_images(product_id)
