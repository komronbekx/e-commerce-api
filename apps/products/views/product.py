import uuid
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import ProductService
from ..serializers import ProductSerializer
from ..container import get_product_service
from ..swagger.product import (
    list_products_schema,
    get_products_schema,
    create_products_schema,
    update_products_schema,
    delete_products_schema,
)


class ProductView(APIView):
    service: ProductService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_product_service()

    @list_products_schema
    def get(self, request: Request) -> Response:
        products = self.service.get_products()
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data)

    @create_products_schema
    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_product = self.service.create_product(serializer.validated_data)
        return Response(
            ProductSerializer(created_product, context={"request": request}).data,
            status=status.HTTP_201_CREATED,
        )


class ProductDetailView(APIView):
    service: ProductService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_product_service()

    @get_products_schema
    def get(self, request: Request, product_id: uuid.UUID) -> Response:
        product = self.service.get_product(product_id)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @update_products_schema
    def put(self, request: Request, product_id: uuid.UUID) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_product = self.service.update_product(
            product_id, serializer.validated_data
        )
        return Response(
            ProductSerializer(updated_product, context={"request": request}).data,
            status=status.HTTP_200_OK,
        )

    @delete_products_schema
    def delete(self, request: Request, product_id: uuid.UUID) -> Response:
        self.service.delete_product(product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
