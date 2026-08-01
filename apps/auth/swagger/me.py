from apps.auth.serializers.me import MeUpdateSerializer
from drf_spectacular.utils import extend_schema

get_me_schema_swagger = extend_schema(
    summary="Get me",
    request=MeUpdateSerializer,
    responses={200: MeUpdateSerializer},
    tags=["authentication"],
)

update_me_schema_swagger = extend_schema(
    summary="Update Me",
    request=MeUpdateSerializer,
    responses={200: MeUpdateSerializer},
    tags=["authentication"],
)
