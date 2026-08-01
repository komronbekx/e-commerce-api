from apps.auth.dto import LoginRequestDTO
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict) -> LoginRequestDTO:
        return LoginRequestDTO(email=attrs["email"], password=attrs["password"])
