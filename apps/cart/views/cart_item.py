import uuid

from apps.cart.container import get_cart_service
from apps.cart.serializers import (
    AddCartItemSerializer,
    CartItemSerializer,
    UpdateCartItemSerializer,
)
from apps.cart.services import CartService
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.cart.swagger.schemas import add_cart_item_schema
from apps.cart.swagger.schemas import remove_cart_item_schema, update_cart_item_schema


class CartItemView(APIView):
    permission_classes = [IsAuthenticated]
    service: CartService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_cart_service()

    @add_cart_item_schema
    def post(self, request: Request) -> Response:
        serializer = AddCartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = self.service.add_item(
            request.user,  # type: ignore
            serializer.validated_data["product_id"],
            serializer.validated_data["quantity"],
        )
        return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)


class CartItemDetailView(APIView):
    permission_classes = [IsAuthenticated]
    service: CartService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_cart_service()

    @update_cart_item_schema
    def patch(self, request: Request, item_id: uuid.UUID) -> Response:
        serializer = UpdateCartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = self.service.update_item_quantity(
            request.user, item_id, serializer.validated_data["quantity"]  # type: ignore
        )
        return Response(CartItemSerializer(item).data, status=status.HTTP_200_OK)

    @remove_cart_item_schema
    def delete(self, request: Request, item_id: uuid.UUID) -> Response:
        self.service.remove_item(request.user, item_id)  # type: ignore
        return Response(status=status.HTTP_204_NO_CONTENT)
