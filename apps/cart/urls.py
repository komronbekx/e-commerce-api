from django.urls import path

from apps.cart.views import CartItemDetailView, CartItemView, CartView

urlpatterns = [
    path("carts/", CartView.as_view(), name="cart"),
    path("carts/items/", CartItemView.as_view(), name="cart-items"),
    path(
        "carts/items/<uuid:item_id>/",
        CartItemDetailView.as_view(),
        name="cart-item-detail",
    ),
]
