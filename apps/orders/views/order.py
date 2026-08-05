import uuid

from apps.orders.container import get_order_service
from apps.orders.serializers import (
    OrderListSerializer,
    OrderSerializer,
    UpdateOrderStatusSerializer,
)
from apps.orders.services import OrderService
from apps.orders.swagger.schemas import (
    list_orders_schema,
    get_order_schema,
    update_order_status_schema,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]
    service: OrderService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_order_service()

    @list_orders_schema
    def get(self, request: Request) -> Response:
        orders = self.service.get_user_orders(request.user)  # type: ignore
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
    service: OrderService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_order_service()

    def get_permissions(self) -> list:
        if self.request.method == "PATCH":
            return [IsAdminUser()]
        return [IsAuthenticated()]

    @get_order_schema
    def get(self, request: Request, order_id: uuid.UUID) -> Response:
        order = self.service.get_order_by_id(order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @update_order_status_schema
    def patch(self, request: Request, order_id: uuid.UUID) -> Response:
        order = self.service.get_order_by_id(order_id)
        serializer = UpdateOrderStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_order = self.service.update_status(
            order, serializer.validated_data["status"]
        )
        return Response(OrderSerializer(updated_order).data, status=status.HTTP_200_OK)
