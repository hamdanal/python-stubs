from collections.abc import Sequence
from typing import Any

from django.db.models import Combinable, Index

class ConditionalUniqueIndex(Index):
    sql_create_index: str
    def __init__(self, condition: str, fields: Sequence[str] = [], name: str | None = None) -> None: ...
    def deconstruct(self) -> tuple[str, tuple[Combinable, ...], dict[str, Any]]: ...
