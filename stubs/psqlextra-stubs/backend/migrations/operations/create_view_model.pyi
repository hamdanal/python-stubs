from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from typing import Any

from django.db.migrations.operations.models import CreateModel
from django.db.migrations.state import ProjectState
from django.db.models import Field

class PostgresCreateViewModel(CreateModel):
    serialization_expand_args: list[str]
    view_options: Mapping[Incomplete, Incomplete]
    def __init__(
        self,
        name: str,
        fields: Sequence[tuple[str, Field[Any, Any]]],
        options: Incomplete | None = None,
        view_options={},
        bases: Mapping[Incomplete, Incomplete] | None = None,
        managers: Incomplete | None = None,
    ) -> None: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def deconstruct(self): ...
