from apps.orders.swagger.schemas import checkout_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.container import get_order_service
from apps.orders.serializers import CheckoutSerializer, OrderSerializer
from apps.orders.services import OrderService


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]
    service: OrderService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_order_service()

    @checkout_schema
    def post(self, request: Request) -> Response:
        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.service.checkout(
            request.user, serializer.validated_data["shipping_address"]  # type: ignore
        )
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
