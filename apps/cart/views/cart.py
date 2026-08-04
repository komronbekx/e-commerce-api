from apps.cart.swagger.schemas import get_cart_schema, clear_cart_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.cart.container import get_cart_service
from apps.cart.serializers import CartSerializer
from apps.cart.services import CartService


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    service: CartService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_cart_service()

    @get_cart_schema
    def get(self, request: Request) -> Response:
        cart = self.service.get_cart(request.user)  # type: ignore
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @clear_cart_schema
    def delete(self, request: Request) -> Response:
        self.service.clear_cart(request.user)  # type: ignore
        return Response(status=status.HTTP_204_NO_CONTENT)
