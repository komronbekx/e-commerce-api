from django.urls import path

from apps.cart.views import CartItemDetailView, CartItemView, CartView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("items/", CartItemView.as_view(), name="cart-items"),
    path("items/<uuid:item_id>/", CartItemDetailView.as_view(), name="cart-item-detail"),
]
