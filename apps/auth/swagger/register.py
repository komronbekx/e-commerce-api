from apps.auth.serializers.register import RegisterSerializer
from drf_spectacular.utils import extend_schema

register_schema_swagger = extend_schema(
    summary="Login",
    request=RegisterSerializer,
    responses={201: RegisterSerializer},
    tags=["authentication"],
)
