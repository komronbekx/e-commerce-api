from rest_framework import serializers
from ..models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "product", "is_primary", "image", "order")


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category_id = serializers.UUIDField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "category_id",
            "description",
            "images",
            "price",
            "stock",
            "is_active",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
