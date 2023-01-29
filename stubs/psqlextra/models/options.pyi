from _typeshed import Incomplete

from psqlextra.types import PostgresPartitioningMethod, SQLWithParams as SQLWithParams

class PostgresPartitionedModelOptions:
    method: Incomplete
    key: Incomplete
    original_attrs: Incomplete
    def __init__(self, method: PostgresPartitioningMethod, key: list[str]) -> None: ...

class PostgresViewOptions:
    query: Incomplete
    original_attrs: Incomplete
    def __init__(self, query: SQLWithParams | None) -> None: ...
