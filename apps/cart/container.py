from apps.cart.repositories import CartRepository
from apps.cart.services import CartService
from apps.products.container import get_product_service


def get_cart_service() -> CartService:
    return CartService(
        repo=CartRepository(),
        product_service=get_product_service(),
    )
