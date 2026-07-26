import uuid
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import CategorySerializer
from ..container import get_category_service
from ..services import CategoryService
from ..swagger.category import (
    list_categories_schema,
    get_category_schema,
    create_category_schema,
    update_category_schema,
    delete_category_schema,
)


class CategoryView(APIView):
    service: CategoryService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_category_service()

    @list_categories_schema
    def get(self, request: Request) -> Response:
        categories = self.service.get_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @create_category_schema
    def post(self, request: Request) -> Response:
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_categories = self.service.create_category(serializer.validated_data)
        return Response(
            CategorySerializer(created_categories).data, status=status.HTTP_201_CREATED
        )


class CategoryDetailView(APIView):
    service: CategoryService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_category_service()

    @get_category_schema
    def get(self, request: Request, category_id: uuid.UUID) -> Response:
        category = self.service.get_category_by_id(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @update_category_schema
    def put(self, request: Request, category_id: uuid.UUID) -> Response:
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = self.service.get_category_by_id(category_id)
        category.name = serializer.validated_data.get("name")
        category.slug = serializer.validated_data.get("slug")
        updated_category = self.service.update_category(category_id, category)
        return Response(
            CategorySerializer(updated_category).data, status=status.HTTP_200_OK
        )

    @delete_category_schema
    def delete(self, request: Request, category_id: uuid.UUID) -> Response:
        self.service.delete_category(category_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
