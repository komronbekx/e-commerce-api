from rest_framework import serializers

from apps.orders.models import OrderItem
from apps.products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "product", "quantity", "price")
        read_only_fields = ("id", "product", "quantity", "price")


class CheckoutSerializer(serializers.Serializer):
    shipping_address = serializers.CharField()

    def validate(self, attrs: dict) -> dict:
        return {"shipping_address": attrs["shipping_address"]}
