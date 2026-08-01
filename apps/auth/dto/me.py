from typing import TypedDict


class MeUpdateRequestDTO(TypedDict, total=False):
    first_name: str
    last_name: str
