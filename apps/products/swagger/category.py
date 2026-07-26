from ..serializers import CategorySerializer
from drf_spectacular.utils import extend_schema

list_categories_schema = extend_schema(
    summary="List all categories",
    description="List all categories",
    responses={
        200: CategorySerializer(many=True),
    },
    tags=["categories"],
)

get_category_schema = extend_schema(
    summary="Get one category",
    description="Get one category by its id",
    responses={200: CategorySerializer()},
    tags=["categories"],
)

create_category_schema = extend_schema(
    summary="Create a new category",
    description="Create a new category",
    request=CategorySerializer,
    responses={201: CategorySerializer()},
    tags=["categories"],
)

update_category_schema = extend_schema(
    summary="Update a category",
    description="Update a category by its id",
    request=CategorySerializer,
    responses={200: CategorySerializer()},
    tags=["categories"],
)

delete_category_schema = extend_schema(
    summary="Delete a category",
    description="Delete a category by its id",
    request=CategorySerializer,
    responses={204: None},
    tags=["categories"],
)
