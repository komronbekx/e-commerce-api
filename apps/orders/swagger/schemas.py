from drf_spectacular.utils import extend_schema

from apps.orders.serializers import (
    CheckoutSerializer,
    OrderListSerializer,
    OrderSerializer,
    UpdateOrderStatusSerializer,
)

checkout_schema = extend_schema(
    summary="Checkout cart",
    description="Convert the current user's cart into an order. Cart must not be empty.",
    request=CheckoutSerializer,
    responses={201: OrderSerializer()},
    tags=["orders"],
)

list_orders_schema = extend_schema(
    summary="List user's orders",
    description="List all orders belonging to the currently authenticated user",
    responses={200: OrderListSerializer(many=True)},
    tags=["orders"],
)

get_order_schema = extend_schema(
    summary="Get order details",
    description="Retrieve a single order by its id, including all order items",
    responses={200: OrderSerializer()},
    tags=["orders"],
)

update_order_status_schema = extend_schema(
    summary="Update order status",
    description="Update the status of an order. Only accessible by admin/staff users.",
    request=UpdateOrderStatusSerializer,
    responses={200: OrderSerializer()},
    tags=["orders"],
)
