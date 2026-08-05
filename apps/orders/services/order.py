import uuid
from decimal import Decimal

from django.db import transaction
from apps.cart.services import CartService
from apps.products.repositories import ProductRepository
from apps.users.models import User
from django.db.models.query import QuerySet
from ..exceptions import EmptyCart, InsufficientStock, OrderNotFound
from ..models import Order, OrderItem, OrderStatus
from ..repositories import OrderRepository


class OrderService:
    def __init__(
        self,
        repo: OrderRepository,
        product_repo: ProductRepository,
        cart_service: CartService,
    ) -> None:
        self.repo = repo
        self.product_repo = product_repo
        self.cart_service = cart_service

    def get_order_by_id(self, order_id: uuid.UUID) -> Order:
        order = self.repo.get_order_by_id(order_id)
        if not order:
            raise OrderNotFound(f"Order with id {order_id} not found")
        return order

    def get_user_orders(self, user: User) -> QuerySet[Order]:
        return self.repo.get_orders_by_user(user)

    def update_status(self, order: Order, status: OrderStatus) -> Order:
        order.status = status
        self.repo.update_order(order)
        return order

    @transaction.atomic
    def checkout(self, user: User, shipping_address: str) -> Order:
        cart_items = self.cart_service.get_cart_items(user)

        if not cart_items:
            raise EmptyCart("Cannot checkout with an empty cart")

        order = Order(
            user=user,
            status=OrderStatus.PENDING,
            total_price=0,
            shipping_address=shipping_address,
        )
        self.repo.create_order(order)

        total_price = Decimal("0")

        for item in cart_items:
            product = self.product_repo.get_product_by_id(item.product_id)

            if not product:
                raise InsufficientStock(f"Product {item.product_id} no longer exists")

            success = self.product_repo.decrease_stock(product.id, item.quantity)
            if not success:
                raise InsufficientStock(
                    f"Insufficient stock for product '{product.name}'"
                )

            order_item = OrderItem(
                order=order,
                product=product,
                quantity=item.quantity,
                price=product.price,
            )
            self.repo.create_order_item(order_item)
            total_price += product.price * item.quantity

        order.total_price = total_price
        self.repo.update_order(order)

        self.cart_service.clear_cart(user)

        return order
