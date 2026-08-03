from drf_spectacular.utils import extend_schema

from apps.cart.serializers import (
    AddCartItemSerializer,
    CartItemSerializer,
    CartSerializer,
    UpdateCartItemSerializer,
)

get_cart_schema = extend_schema(
    summary="Get current user's cart",
    description="Retrieve the cart belonging to the currently authenticated user",
    responses={200: CartSerializer()},
    tags=["cart"],
)

clear_cart_schema = extend_schema(
    summary="Clear the cart",
    description="Remove all items from the current user's cart",
    responses={204: None},
    tags=["cart"],
)

add_cart_item_schema = extend_schema(
    summary="Add item to cart",
    description="Add a product to the cart, or increase quantity if it already exists",
    request=AddCartItemSerializer,
    responses={201: CartItemSerializer()},
    tags=["cart"],
)

update_cart_item_schema = extend_schema(
    summary="Update cart item quantity",
    description="Update the quantity of an existing cart item",
    request=UpdateCartItemSerializer,
    responses={200: CartItemSerializer()},
    tags=["cart"],
)

remove_cart_item_schema = extend_schema(
    summary="Remove cart item",
    description="Remove a single item from the cart",
    responses={204: None},
    tags=["cart"],
)
