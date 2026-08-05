from apps.cart.container import get_cart_service
from apps.orders.repositories import OrderRepository
from apps.orders.services import OrderService
from apps.products.repositories import ProductRepository


def get_order_service() -> OrderService:
    return OrderService(
        repo=OrderRepository(),
        product_repo=ProductRepository(),
        cart_service=get_cart_service(),
    )
