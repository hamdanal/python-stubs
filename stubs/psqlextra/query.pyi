from collections.abc import Sequence
from typing import Any, Literal, TypeVar, overload
from typing_extensions import Self, TypeAlias

from django.db import models
from django.db.models import Expression, Q
from psqlextra.types import ConflictAction

_T = TypeVar("_T", bound=models.Model)

_Rows: TypeAlias = list[dict[str, Any]]
ConflictTarget: TypeAlias = Sequence[str | tuple[str, ...]]

class PostgresQuerySet(models.QuerySet[_T]):
    def rename_annotations(self, **annotations: str) -> Self: ...
    def on_conflict(
        self,
        fields: ConflictTarget,
        action: ConflictAction,
        *,
        index_predicate: Expression | Q | str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> _PostgresQuerySetWithConflict[_T]: ...
    def bulk_insert(self, rows: _Rows, *, return_model: bool = False, using: str | None = None) -> list[_T]: ...
    def insert(self, using: str | None = None, **fields: Any) -> int: ...
    def insert_and_get(self, using: str | None = None, **fields) -> _T: ...
    def upsert(
        self,
        conflict_target: ConflictTarget,
        fields: dict[str, Any],
        *,
        index_predicate: Expression | Q | str | None = None,
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> int | None: ...
    def upsert_and_get(
        self,
        conflict_target: ConflictTarget,
        fields: dict[str, Any],
        *,
        index_predicate: Expression | Q | str | None = None,
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> _T | None: ...
    @overload
    def bulk_upsert(
        self,
        conflict_target: ConflictTarget,
        rows: _Rows,
        *,
        index_predicate: Expression | Q | str | None = None,
        return_model: Literal[False] = False,
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> _Rows: ...
    @overload
    def bulk_upsert(
        self,
        conflict_target: ConflictTarget,
        rows: _Rows,
        *,
        index_predicate: Expression | Q | str | None = None,
        return_model: Literal[True],
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> list[_T]: ...
    @overload
    def bulk_upsert(
        self,
        conflict_target: ConflictTarget,
        rows: _Rows,
        *,
        index_predicate: Expression | Q | str | None = None,
        return_model: bool = False,
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> list[_T] | _Rows: ...

class _PostgresQuerySetWithConflict(PostgresQuerySet[_T]):
    # This class does not exist at runtime. It is used to describe the behavior of the
    # PostgresQuerySet when conflict_target and conflict_action are set. If these two attributes
    # are not set, PostgresQuerySet uses the default behavior of Django's QuerySet; otherwise,
    # it uses the behavior defined in this class.
    @overload  # type: ignore[override]
    def bulk_insert(self, rows: _Rows, *, return_model: Literal[False] = False, using: str | None = None) -> _Rows: ...
    @overload
    def bulk_insert(self, rows: _Rows, *, return_model: Literal[True], using: str | None = None) -> list[_T]: ...
    @overload
    def bulk_insert(self, rows: _Rows, *, return_model: bool = False, using: str | None = None) -> list[_T] | _Rows: ...
    def insert(self, using: str | None = None, **fields: Any) -> int | None: ...  # type: ignore[override]
    def insert_and_get(self, using: str | None = None, **fields) -> _T | None: ...
