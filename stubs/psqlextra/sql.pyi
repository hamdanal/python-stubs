from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any

from django.db.models import Model
from django.db.models.fields import Field
from django.db.models.sql import InsertQuery, Query, UpdateQuery
from psqlextra.compiler import PostgresInsertOnConflictCompiler, SQLUpdateCompiler as PostgresUpdateCompiler
from psqlextra.types import ConflictAction

class PostgresQuery(Query):
    def rename_annotations(self, annotations: dict[str, str]) -> None: ...
    def _is_hstore_field(self, field_name: str) -> tuple[bool, Field[Any, Any] | None]: ...

class PostgresInsertQuery(InsertQuery):
    conflict_target: list[str | tuple[str, ...]]
    conflict_action: ConflictAction
    conflict_update_condition: Incomplete | None
    index_predicate: Incomplete | None
    update_fields: list[Field[Any, Any]]

    def values(
        self, objs: list[Model], insert_fields: Iterable[Field[Any, Any]], update_fields: list[Field[Any, Any]] | None = ...
    ) -> None: ...
    def get_compiler(self, using: str | None = None, connection: Incomplete = None) -> PostgresInsertOnConflictCompiler: ...

class PostgresUpdateQuery(UpdateQuery):
    def get_compiler(self, using: str | None = None, connection: Incomplete = None) -> PostgresUpdateCompiler: ...
