from apps.auth.container import get_me_service
from apps.auth.serializers.me import MeUpdateSerializer
from apps.auth.services.me import MeService
from apps.auth.swagger.me import get_me_schema_swagger, update_me_schema_swagger
from apps.users.user_serializer import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class MeView(APIView):
    permission_classes = [IsAuthenticated]
    service: MeService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_me_service()

    @get_me_schema_swagger
    def get(self, request: Request) -> Response:
        user = self.service.get_me(request.user.id)  # type: ignore[arg-type]
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @update_me_schema_swagger
    def patch(self, request: Request) -> Response:
        serializer = MeUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user = self.service.update_me(request.user.id, serializer.validated_data)  # type: ignore[arg-type]
        return Response(UserSerializer(updated_user).data, status=status.HTTP_200_OK)
