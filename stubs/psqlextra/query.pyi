from collections.abc import Iterable, Sequence
from typing import Any, Generic, Literal, overload
from typing_extensions import Self, TypeAlias, TypeVar

from django.db import models
from django.db.models import Expression, Q
from django.db.models.constraints import BaseConstraint
from django.db.models.indexes import Index
from psqlextra.sql import PostgresQuery
from psqlextra.types import ConflictAction

ConflictTarget: TypeAlias = Sequence[str | tuple[str, ...]] | BaseConstraint | Index

_ModelT = TypeVar("_ModelT", bound=models.Model)
_TargetT = TypeVar("_TargetT", bound=ConflictTarget | None, default=None)
_ActionT = TypeVar("_ActionT", bound=ConflictAction | None, default=None)

class PostgresQuerySet(models.QuerySet[_ModelT], Generic[_ModelT, _TargetT, _ActionT]):
    query: PostgresQuery
    conflict_target: _TargetT
    conflict_action: _ActionT
    conflict_update_condition: Expression | Q | str | None
    index_predicate: Expression | Q | str | None
    update_values: dict[str, Any]
    def annotate(self, **annotations: Any) -> Self: ...  # type: ignore[override]
    def rename_annotations(self, **annotations: str) -> Self: ...
    # Calling on_conflict on a queryset without a conflict target or action fills in the
    # conflict target and action for the queryset (cf. first overload).
    @overload
    def on_conflict(
        self: PostgresQuerySet[_ModelT, None, None],
        fields: ConflictTarget,
        action: ConflictAction,
        index_predicate: Expression | Q | str | None = None,
        update_condition: Expression | Q | str | None = None,
        update_values: dict[str, Any | Expression] | None = None,
    ) -> PostgresQuerySet[_ModelT, ConflictTarget, ConflictAction]: ...
    @overload
    def on_conflict(
        self,
        fields: ConflictTarget,
        action: ConflictAction,
        index_predicate: Expression | Q | str | None = None,
        update_condition: Expression | Q | str | None = None,
        update_values: dict[str, Any | Expression] | None = None,
    ) -> Self: ...
    # Whether bulk_insert returns models or dictionaries depends on:
    # - If the queryset does not have a conflict target or action, it always returns models.
    # - If the queryset has a conflict target or action, it returns models if return_model is
    #   True, and dictionaries if return_model is False.
    @overload
    def bulk_insert(
        self: PostgresQuerySet[_ModelT, None, None],
        rows: Iterable[dict[str, Any]],
        return_model: bool = False,
        using: str | None = None,
    ) -> list[_ModelT]: ...
    @overload
    def bulk_insert(
        self: PostgresQuerySet[_ModelT, ConflictTarget, ConflictAction],
        rows: Iterable[dict[str, Any]],
        return_model: Literal[True],
        using: str | None = None,
    ) -> list[_ModelT]: ...
    @overload
    def bulk_insert(
        self: PostgresQuerySet[_ModelT, ConflictTarget, ConflictAction],
        rows: Iterable[dict[str, Any]],
        return_model: Literal[False] = False,
        using: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    def bulk_insert(
        self: PostgresQuerySet[_ModelT, ConflictTarget, ConflictAction],
        rows: Iterable[dict[str, Any]],
        return_model: bool = False,
        using: str | None = None,
    ) -> list[_ModelT] | list[dict[str, Any]]: ...
    def insert(self, using: str | None = None, **fields: Any) -> Any: ...
    def insert_and_get(self, using: str | None = None, **fields) -> _ModelT: ...
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
    ) -> _ModelT | None: ...
    @overload
    def bulk_upsert(
        self,
        conflict_target: ConflictTarget,
        rows: Iterable[dict[str, Any]],
        index_predicate: Expression | Q | str | None = None,
        *,
        return_model: Literal[True],
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> list[_ModelT]: ...
    @overload
    def bulk_upsert(
        self,
        conflict_target: ConflictTarget,
        rows: Iterable[dict[str, Any]],
        index_predicate: Expression | Q | str | None = None,
        return_model: Literal[False] = False,
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    def bulk_upsert(
        self,
        conflict_target: ConflictTarget,
        rows: Iterable[dict[str, Any]],
        index_predicate: Expression | Q | str | None = None,
        return_model: bool = False,
        using: str | None = None,
        update_condition: Expression | Q | str | None = None,
    ) -> list[_ModelT] | list[dict[str, Any]]: ...
