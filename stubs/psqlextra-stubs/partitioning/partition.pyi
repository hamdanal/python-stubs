from abc import ABCMeta, abstractmethod
from typing import Any

from psqlextra.backend.schema import PostgresSchemaEditor
from psqlextra.models import PostgresPartitionedModel

class PostgresPartition(metaclass=ABCMeta):
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def create(self, model: PostgresPartitionedModel, schema_editor: PostgresSchemaEditor, comment: str | None = ...) -> None: ...
    @abstractmethod
    def delete(self, model: PostgresPartitionedModel, schema_editor: PostgresSchemaEditor) -> None: ...
    def deconstruct(self) -> dict[str, Any]: ...
