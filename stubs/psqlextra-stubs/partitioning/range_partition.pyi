import abc
from typing import Any

from psqlextra.backend.schema import PostgresSchemaEditor
from psqlextra.models import PostgresPartitionedModel
from psqlextra.partitioning.partition import PostgresPartition

class PostgresRangePartition(PostgresPartition, metaclass=abc.ABCMeta):
    from_values: Any
    to_values: Any
    def __init__(self, from_values: Any, to_values: Any) -> None: ...
    def deconstruct(self) -> dict[str, Any]: ...
    def create(
        self, model: PostgresPartitionedModel, schema_editor: PostgresSchemaEditor, comment: str | None = None
    ) -> None: ...
    def delete(self, model: PostgresPartitionedModel, schema_editor: PostgresSchemaEditor) -> None: ...
