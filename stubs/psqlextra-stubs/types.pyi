from enum import Enum
from typing import Any
from typing_extensions import TypeAlias

SQL: TypeAlias = str
SQLWithParams: TypeAlias = tuple[str, tuple[Any, ...] | dict[str, Any]]

class StrEnum(str, Enum):  # type: ignore[misc]
    @classmethod
    def all(cls) -> list[StrEnum]: ...
    @classmethod
    def values(cls) -> list[str]: ...

class ConflictAction(Enum):
    NOTHING = "NOTHING"
    UPDATE = "UPDATE"

    @classmethod
    def all(cls) -> list[ConflictAction]: ...

class PostgresPartitioningMethod(StrEnum):
    RANGE = "range"
    LIST = "list"
    HASH = "hash"
