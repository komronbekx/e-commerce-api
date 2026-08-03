import uuid
from apps.cart.exceptions.cart_item_not_found import CartItemNotFound
from apps.cart.models import Cart, CartItem
from apps.cart.repositories import CartRepository
from apps.products.services import ProductService
from apps.users.models import User


class CartService:
    def __init__(self, repo: CartRepository, product_service: ProductService) -> None:
        self.repo = repo
        self.product_service = product_service

    def get_cart(self, user: User) -> Cart:
        return self.repo.get_or_create_cart(user)

    def get_cart_items(self, user: User) -> list[CartItem]:
        cart = self.repo.get_or_create_cart(user)
        return list(self.repo.get_items(cart.id))

    def add_item(self, user: User, product_id: uuid.UUID, quantity: int) -> CartItem:
        self.product_service.get_product(product_id)

        cart = self.repo.get_or_create_cart(user)
        existing_item = self.repo.get_item(cart.id, product_id)

        if existing_item:
            new_quantity = existing_item.quantity + quantity
            return self.repo.update_item_quantity(existing_item, new_quantity)

        return self.repo.add_item(cart.id, product_id, quantity)

    def update_item_quantity(
        self, user: User, item_id: uuid.UUID, quantity: int
    ) -> CartItem:
        cart = self.repo.get_or_create_cart(user)
        item = self.repo.get_item_by_id(item_id)

        if not item or item.cart_id != cart.id:
            raise CartItemNotFound(f"Cart item with id {item_id} was not found")

        return self.repo.update_item_quantity(item, quantity)

    def remove_item(self, user: User, item_id: uuid.UUID) -> None:
        cart = self.repo.get_or_create_cart(user)
        item = self.repo.get_item_by_id(item_id)

        if not item or item.cart_id != cart.id:
            raise CartItemNotFound(f"Cart item with id {item_id} was not found")

        self.repo.remove_item(item_id)

    def clear_cart(self, user: User) -> None:
        cart = self.repo.get_or_create_cart(user)
        self.repo.clear_cart(cart.id)
