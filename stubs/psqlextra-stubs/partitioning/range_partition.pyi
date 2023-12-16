import abc
from _typeshed import Incomplete
from typing import Any

from psqlextra.backend.schema import PostgresSchemaEditor
from psqlextra.models import PostgresPartitionedModel
from psqlextra.partitioning.partition import PostgresPartition

class PostgresRangePartition(PostgresPartition, metaclass=abc.ABCMeta):
    from_values: Incomplete
    to_values: Incomplete
    def __init__(self, from_values: Any, to_values: Any) -> None: ...
    def deconstruct(self) -> dict: ...
    def create(self, model: PostgresPartitionedModel, schema_editor: PostgresSchemaEditor, comment: str | None = ...) -> None: ...
    def delete(self, model: PostgresPartitionedModel, schema_editor: PostgresSchemaEditor) -> None: ...
