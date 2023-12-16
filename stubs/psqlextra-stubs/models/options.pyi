from psqlextra.types import PostgresPartitioningMethod, SQLWithParams

class PostgresPartitionedModelOptions:
    method: PostgresPartitioningMethod
    key: list[str]
    original_attrs: dict[str, PostgresPartitioningMethod | list[str]]
    def __init__(self, method: PostgresPartitioningMethod, key: list[str]) -> None: ...

class PostgresViewOptions:
    query: SQLWithParams | None
    original_attrs: dict[str, SQLWithParams | None]
    def __init__(self, query: SQLWithParams | None) -> None: ...
