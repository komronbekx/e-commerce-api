from apps.auth.container import get_auth_service
from apps.auth.serializers.logout import LogoutSerializer
from apps.auth.services.auth import AuthService
from apps.auth.swagger.logout import logout_schema_swagger
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    service: AuthService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_auth_service()

    @logout_schema_swagger
    def post(self, request: Request) -> Response:
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.service.logout(serializer.validated_data)
        return Response(status=status.HTTP_204_NO_CONTENT)
