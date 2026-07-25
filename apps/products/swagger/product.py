from ..serializers import ProductSerializer, ProductImageSerializer
from drf_spectacular.utils import extend_schema

list_products_schema = extend_schema(
    summary="List all products",
    description="List all products",
    responses={
        200: ProductSerializer(many=True),
    },
    tags=["products"],
)

get_products_schema = extend_schema(
    summary="Get one products",
    description="Get one products by its id",
    responses={200: ProductSerializer()},
    tags=["products"],
)

create_products_schema = extend_schema(
    summary="Create a new products",
    description="Create a new products",
    request=ProductSerializer,
    responses={201: ProductSerializer()},
    tags=["products"],
)

update_products_schema = extend_schema(
    summary="Update a products",
    description="Update a products by its id",
    request=ProductSerializer,
    responses={200: ProductSerializer()},
    tags=["products"],
)

delete_products_schema = extend_schema(
    summary="Delete a products",
    description="Delete a products by its id",
    request=ProductSerializer,
    responses={204: None},
    tags=["products"],
)

list_product_images_schema = extend_schema(
    summary="List all product images",
    description="List all product images",
    responses={
        200: ProductImageSerializer(many=True),
    },
    tags=["product-images"],
)

get_product_images_schema = extend_schema(
    summary="Get one product images",
    description="Get one product images by its id",
    responses={200: ProductImageSerializer()},
    tags=["product-images"],
)

create_product_images_schema = extend_schema(
    summary="Create a new product images",
    description="Create a new product images",
    request=ProductImageSerializer,
    responses={201: ProductImageSerializer()},
    tags=["product-images"],
)

update_product_images_schema = extend_schema(
    summary="Update a product images",
    description="Update a product images by its id",
    request=ProductImageSerializer,
    responses={200: ProductImageSerializer()},
    tags=["product-images"],
)

delete_product_images_schema = extend_schema(
    summary="Delete a product images",
    description="Delete a product images by its id",
    request=ProductImageSerializer,
    responses={204: None},
    tags=["product-images"],
)
