from typing import Any

from django.db.migrations.operations.base import Operation

class PostgresPartitionOperation(Operation):
    model_name: str
    model_name_lower: str
    name: str
    def __init__(self, model_name: str, name: str) -> None: ...
    def deconstruct(self) -> tuple[str, list[Any], dict[str, Any]]: ...
    def state_forwards(self, *args, **kwargs) -> None: ...
    def state_backwards(self, *args, **kwargs) -> None: ...
    def reduce(self, *args, **kwargs) -> bool: ...
