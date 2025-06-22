from _typeshed import Incomplete

from django.db.migrations.operations.models import CreateModel

class PostgresCreatePartitionedModel(CreateModel):
    serialization_expand_args: Incomplete
    partitioning_options: Incomplete
    def __init__(
        self,
        name,
        fields,
        options: Incomplete | None = None,
        partitioning_options={},
        bases: Incomplete | None = None,
        managers: Incomplete | None = None,
    ) -> None: ...
    def state_forwards(self, app_label, state) -> None: ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def deconstruct(self): ...
    def reduce(self, *args, **kwargs): ...
