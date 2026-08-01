from apps.auth.dto import LogoutRequestDTO
from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs: dict) -> LogoutRequestDTO:
        return LogoutRequestDTO(refresh_token=attrs["refresh_token"])
