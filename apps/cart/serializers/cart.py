from rest_framework import serializers

from apps.cart.models import Cart

from .cart_item import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("id", "items", "total_price", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    def get_total_price(self, obj: Cart) -> str:
        total = sum(item.product.price * item.quantity for item in obj.items.all())
        return str(total)
