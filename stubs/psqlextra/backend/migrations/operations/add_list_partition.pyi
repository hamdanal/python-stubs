from _typeshed import Incomplete

from .partition import PostgresPartitionOperation

class PostgresAddListPartition(PostgresPartitionOperation):
    values: Incomplete
    def __init__(self, model_name, name, values) -> None: ...
    def state_forwards(self, app_label, state) -> None: ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def deconstruct(self): ...
    def describe(self) -> str: ...