from apps.auth.serializers.login import LoginSerializer
from drf_spectacular.utils import extend_schema

login_schema_swagger = extend_schema(
    summary="Login",
    request=LoginSerializer,
    responses={200: LoginSerializer},
    tags=["authentication"],
)


