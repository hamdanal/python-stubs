from django.db.migrations.operations.base import Operation

class ApplyState(Operation):
    reduces_to_sql: bool
    state_operation: Operation
    def __init__(self, state_operation: Operation) -> None: ...
    def deconstruct(self): ...
    @property
    def reversible(self) -> bool: ...  # type: ignore[override]
    def state_forwards(self, app_label, state) -> None: ...
    def state_backwards(self, app_label, state) -> None: ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
