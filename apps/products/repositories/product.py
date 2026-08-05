from django.core.files import File
from django.db import models
from django.db.models import QuerySet
from ..models import Product, ProductImage
import uuid


class ProductRepository:
    def get_all_products(self) -> QuerySet[Product]:
        return Product.objects.all().order_by("-created_at")

    def get_product_by_id(self, product_id: uuid.UUID) -> Product | None:
        return Product.objects.filter(id=product_id).first()

    def get_product_by_name(self, name: str) -> Product | None:
        return Product.objects.filter(name=name).first()

    def filter_by_category(self, category_id: uuid.UUID) -> QuerySet[Product]:
        return Product.objects.filter(category=category_id).order_by("-created_at")

    def create(self, product: Product) -> Product:
        product.save()
        return product

    def update(self, product: Product) -> Product:
        product.save()
        return product

    def delete(self, product_id: uuid.UUID) -> bool:
        deleted_count, _ = Product.objects.filter(id=product_id).delete()
        return deleted_count > 0

    def get_product_for_update(self, product_id: uuid.UUID) -> Product | None:
        """
        Mahsulotni DB darajasida 'qulflab' oladi (SELECT FOR UPDATE).
        Faqat tranzaksiya ichida chaqirilishi kerak!
        """
        return Product.objects.select_for_update().filter(id=product_id).first()

    def decrease_stock(self, product_id: uuid.UUID, quantity: int) -> bool:
        """
        Stock'ni xavfsiz kamaytiradi — faqat yetarli miqdor bo'lsa.
        Atomic UPDATE orqali, race condition'siz.
        """
        updated_count = Product.objects.filter(id=product_id, stock__gte=quantity).update(
            stock=models.F("stock") - quantity
        )
        return updated_count > 0

    def add_image(
        self, product: Product, image_file: File, is_primary: bool, order: int = 0
    ) -> ProductImage:
        return ProductImage.objects.create(
            product=product, image=image_file, is_primary=is_primary, order=order
        )

    def clear_primary_image(self, product_id: uuid.UUID) -> int:
        return ProductImage.objects.filter(product_id=product_id).update(is_primary=False)

    def delete_image(self, image_id: uuid.UUID) -> bool:
        deleted_count, _ = ProductImage.objects.filter(id=image_id).delete()
        return deleted_count > 0

    def get_images(self, product_id: uuid.UUID) -> QuerySet[ProductImage]:
        return ProductImage.objects.filter(product_id=product_id).order_by("order")
