from apps.auth.dto import RegisterRequestDTO
from apps.users.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")

    def validate(self, attrs: dict) -> RegisterRequestDTO:
        return RegisterRequestDTO(
            email=attrs["email"],
            password=attrs["password"],
            first_name=attrs["first_name"],
            last_name=attrs["last_name"],
        )
