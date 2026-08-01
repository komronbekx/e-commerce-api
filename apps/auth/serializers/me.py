from __future__ import annotations

from apps.auth.dto import MeUpdateRequestDTO
from rest_framework import serializers


class MeUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=False,
        help_text="New User First Name",
    )
    last_name = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=False,
        help_text="New User Last Name",
    )

    def validate(self, attrs: dict) -> MeUpdateRequestDTO:
        return MeUpdateRequestDTO(**attrs)
