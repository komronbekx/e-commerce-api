from rest_framework import serializers

from apps.cart.models import CartItem
from apps.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ("id", "product", "quantity", "created_at")
        read_only_fields = ("id", "created_at")


class AddCartItemSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=1, default=1)

    def validate(self, attrs: dict) -> dict:
        return {
            "product_id": attrs["product_id"],
            "quantity": attrs["quantity"],
        }


class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)

    def validate(self, attrs: dict) -> dict:
        return {"quantity": attrs["quantity"]}
