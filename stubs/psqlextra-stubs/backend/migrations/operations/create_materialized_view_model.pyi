from _typeshed import Incomplete

from django.db.migrations.operations.models import CreateModel

class PostgresCreateMaterializedViewModel(CreateModel):
    serialization_expand_args: Incomplete
    view_options: Incomplete
    def __init__(
        self,
        name,
        fields,
        options: Incomplete | None = ...,
        view_options=...,
        bases: Incomplete | None = ...,
        managers: Incomplete | None = ...,
    ) -> None: ...
    def state_forwards(self, app_label, state) -> None: ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def deconstruct(self): ...
    def describe(self): ...
