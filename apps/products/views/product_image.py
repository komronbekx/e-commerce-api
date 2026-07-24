import uuid
from apps.products.container import get_product_service
from apps.products.serializers import ProductImageSerializer
from apps.products.services import ProductService
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductImageView(APIView):
    service: ProductService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_product_service()

    def get(self, request: Request, product_id: uuid.UUID) -> Response:
        images = self.service.get_product_images(product_id)
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, product_id: uuid.UUID) -> Response:
        image_file = request.FILES.get("image")
        if not image_file:
            return Response(
                {"detail": "Image file is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        is_primary = request.data.get("is_primary", False)
        order = request.data.get("order", 0)

        created_image = self.service.add_product_image(
            product_id=product_id,
            image_file=image_file,
            is_primary=is_primary,
            order=order,
        )
        return Response(
            ProductImageSerializer(created_image).data, status=status.HTTP_201_CREATED
        )


class ProductImageDetailView(APIView):
    service: ProductService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_product_service()

    def delete(
        self, request: Request, product_id: uuid.UUID, image_id: uuid.UUID
    ) -> Response:
        self.service.delete_image(image_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
