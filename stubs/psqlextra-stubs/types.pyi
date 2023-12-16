from enum import Enum
from typing import Any
from typing_extensions import TypeAlias

SQL: TypeAlias = str
SQLWithParams: TypeAlias = tuple[str, tuple[Any, ...] | dict[str, Any]]

class StrEnum(str, Enum):
    @classmethod
    def all(cls) -> list[StrEnum]: ...
    @classmethod
    def values(cls) -> list[str]: ...

class ConflictAction(Enum):
    NOTHING: str
    UPDATE: str

    @classmethod
    def all(cls) -> list[ConflictAction]: ...

class PostgresPartitioningMethod(StrEnum):
    RANGE: str
    LIST: str
    HASH: str
