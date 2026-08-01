from apps.auth.container import get_auth_service
from apps.auth.dto import LoginResponseDTO
from apps.auth.serializers.login import LoginSerializer
from apps.auth.services.auth import AuthService
from apps.auth.swagger.login import login_schema_swagger
from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request


class LoginView(views.APIView):
    permission_classes = [AllowAny]
    service: AuthService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_auth_service()

    @login_schema_swagger
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result: LoginResponseDTO = self.service.login_email(serializer.validated_data)
        return Response(result, status=status.HTTP_200_OK)
