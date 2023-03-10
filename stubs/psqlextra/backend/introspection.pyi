from _typeshed import Incomplete

from psqlextra.types import PostgresPartitioningMethod

PARTITIONING_STRATEGY_TO_METHOD: Incomplete

class PostgresIntrospectedPartitionTable:
    name: str
    full_name: str
    comment: str | None
    def __init__(self, name, full_name, comment) -> None: ...

class PostgresIntrospectedPartitonedTable:
    name: str
    method: PostgresPartitioningMethod
    key: list[str]
    partitions: list[PostgresIntrospectedPartitionTable]
    def partition_by_name(self, name: str) -> PostgresIntrospectedPartitionTable | None: ...
    def __init__(self, name, method, key, partitions) -> None: ...

class PostgresIntrospection:
    def get_partitioned_tables(self, cursor) -> PostgresIntrospectedPartitonedTable: ...
    def get_partitioned_table(self, cursor, table_name: str): ...
    def get_partitions(self, cursor, table_name) -> list[PostgresIntrospectedPartitionTable]: ...
    def get_partition_key(self, cursor, table_name: str) -> list[str]: ...
    def get_constraints(self, cursor, table_name: str): ...
