import uuid

from django.db.models.query import QuerySet

from apps.users.models import User

from ..models import Cart, CartItem


class CartRepository:

    def get_or_create_cart(self, user: User) -> Cart:
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart

    def get_cart_by_user(self, user: User) -> Cart | None:
        return Cart.objects.filter(user=user).first()

    def get_item(self, cart_id: uuid.UUID, product_id: uuid.UUID) -> CartItem | None:
        return CartItem.objects.filter(cart_id=cart_id, product_id=product_id).first()

    def get_items(self, cart_id: uuid.UUID) -> QuerySet[CartItem]:
        return CartItem.objects.filter(cart_id=cart_id).select_related("product")

    def get_item_by_id(self, item_id: uuid.UUID) -> CartItem | None:
        return CartItem.objects.filter(id=item_id).first()

    def add_item(
        self, cart_id: uuid.UUID, product_id: uuid.UUID, quantity: int
    ) -> CartItem:
        return CartItem.objects.create(
            cart_id=cart_id, product_id=product_id, quantity=quantity
        )

    def update_item_quantity(self, item: CartItem, quantity: int) -> CartItem:
        item.quantity = quantity
        item.save()
        return item

    def remove_item(self, item_id: uuid.UUID) -> bool:
        deleted_count, _ = CartItem.objects.filter(id=item_id).delete()
        return deleted_count > 0

    def clear_cart(self, cart_id: uuid.UUID) -> None:
        CartItem.objects.filter(cart_id=cart_id).delete()
