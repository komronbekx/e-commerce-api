from apps.auth.serializers.logout import LogoutSerializer
from drf_spectacular.utils import extend_schema

logout_schema_swagger = extend_schema(
    summary="Logout",
    request=LogoutSerializer,
    responses={200: LogoutSerializer},
    tags=["authentication"],
)
