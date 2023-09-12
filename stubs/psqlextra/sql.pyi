from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any

from django.db.models import Expression, Model, Q
from django.db.models.fields import Field
from django.db.models.sql import InsertQuery, Query, UpdateQuery
from psqlextra.compiler import PostgresInsertOnConflictCompiler, SQLUpdateCompiler as PostgresUpdateCompiler
from psqlextra.types import ConflictAction

class PostgresQuery(Query):
    def rename_annotations(self, annotations: dict[str, str]) -> None: ...

class PostgresInsertQuery(InsertQuery):
    conflict_target: list[str | tuple[str, ...]]
    conflict_action: ConflictAction
    conflict_update_condition: Expression | Q | str | None
    index_predicate: Expression | Q | str | None
    update_values: dict[str, Any | Expression]

    def insert_on_conflict_values(
        self, objs: list[Model], insert_fields: Iterable[Field[Any, Any]], update_values: dict[str, Any | Expression] = {}
    ) -> None: ...
    def get_compiler(self, using: str | None = None, connection: Incomplete = None) -> PostgresInsertOnConflictCompiler: ...

class PostgresUpdateQuery(UpdateQuery):
    def get_compiler(self, using: str | None = None, connection: Incomplete = None) -> PostgresUpdateCompiler: ...
