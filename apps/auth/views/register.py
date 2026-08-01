from apps.auth.container import get_auth_service
from apps.auth.dto.register import RegisterResponseDTO
from apps.auth.serializers.register import RegisterSerializer
from apps.auth.services.auth import AuthService
from apps.auth.swagger.register import register_schema_swagger
from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response


class RegisterView(views.APIView):
    permission_classes = [AllowAny]
    service: AuthService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_auth_service()

    @register_schema_swagger
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result: RegisterResponseDTO = self.service.register_email(serializer.validated_data)
        return Response(result, status=status.HTTP_201_CREATED)
