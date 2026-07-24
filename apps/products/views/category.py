import uuid
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import CategorySerializer
from ..container import get_category_service
from ..services import CategoryService
from ..models import Category
from drf_spectacular.utils import extend_schema


class CategoryView(APIView):
    service: CategoryService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_category_service()

    @extend_schema(responses=CategorySerializer)
    def get(self, request: Request) -> Response:
        categories = self.service.get_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CategorySerializer, responses=CategorySerializer)
    def post(self, request: Request) -> Response:
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = Category(**serializer.validated_data)
        created_categories = self.service.create_category(category)
        return Response(
            CategorySerializer(created_categories).data, status=status.HTTP_201_CREATED
        )


class CategoryDetailView(APIView):
    service: CategoryService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_category_service()

    @extend_schema(responses=CategorySerializer)
    def get(self, request: Request, category_id: uuid.UUID) -> Response:
        category = self.service.get_category_by_id(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
