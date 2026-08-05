from apps.orders.serializers.order_item import OrderItemSerializer
from apps.orders.models import OrderStatus
from rest_framework import serializers
from apps.orders.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "status", "total_price", "created_at")


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "total_price",
            "shipping_address",
            "order_items",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "status",
            "total_price",
            "order_items",
            "created_at",
            "updated_at",
        )


class UpdateOrderStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=OrderStatus.choices)

    def validate(self, attrs: dict) -> dict:
        return {"status": attrs["status"]}
