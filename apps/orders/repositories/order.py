import uuid
from apps.orders.models import Order, OrderItem
from apps.users.models import User
from django.db.models.query import QuerySet


class OrderRepository:
    def create_order(self, order: Order) -> Order:
        order.save()
        return order

    def update_order(self, order: Order) -> Order:
        order.save()
        return order

    def create_order_item(self, order_item: OrderItem) -> OrderItem:
        order_item.save()
        return order_item

    def get_order_by_id(self, order_id: uuid.UUID) -> Order | None:
        return Order.objects.filter(id=order_id).first()

    def get_orders_by_user(self, user: User) -> QuerySet[Order]:
        return Order.objects.filter(user=user).order_by("-created_at")

    def get_order_items(self, order_id: uuid.UUID) -> QuerySet[OrderItem]:
        return OrderItem.objects.filter(order_id=order_id).select_related("product")

    def update_order_status(self, order: Order, status: str) -> Order:
        order.status = status
        order.save()
        return order
