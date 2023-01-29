from _typeshed import Incomplete

from .model import PostgresModelState

class PostgresPartitionState:
    app_label: Incomplete
    model_name: Incomplete
    name: Incomplete
    def __init__(self, app_label: str, model_name: str, name: str) -> None: ...

class PostgresRangePartitionState(PostgresPartitionState):
    from_values: Incomplete
    to_values: Incomplete
    def __init__(self, app_label: str, model_name: str, name: str, from_values, to_values) -> None: ...

class PostgresListPartitionState(PostgresPartitionState):
    values: Incomplete
    def __init__(self, app_label: str, model_name: str, name: str, values) -> None: ...

class PostgresHashPartitionState(PostgresPartitionState):
    modulus: Incomplete
    remainder: Incomplete
    def __init__(self, app_label: str, model_name: str, name: str, modulus: int, remainder: int) -> None: ...

class PostgresPartitionedModelState(PostgresModelState):
    partitions: Incomplete
    partitioning_options: Incomplete
    def __init__(self, *args, partitions: list[PostgresPartitionState] = ..., partitioning_options=..., **kwargs) -> None: ...
    def add_partition(self, partition: PostgresPartitionState): ...
    def delete_partition(self, name: str): ...
