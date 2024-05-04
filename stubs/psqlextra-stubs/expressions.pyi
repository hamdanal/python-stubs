from _typeshed import Incomplete
from typing_extensions import Self

from django.db.models.expressions import Case, Col, Expression, F
from django.db.models.sql.compiler import SQLCompiler

class HStoreValue(Expression):
    value: dict[Incomplete, Incomplete]
    def __init__(self, value: dict[Incomplete, Incomplete]) -> None: ...
    def resolve_expression(self, *args: Incomplete, **kwargs: Incomplete) -> HStoreValue: ...
    def as_sql(self, compiler: SQLCompiler, connection: Incomplete) -> tuple[str, list[Incomplete]]: ...  # type: ignore[override]

class HStoreColumn(Col):
    alias: str
    target: str
    hstore_key: str

    def __init__(self, alias: str, target: str, hstore_key: str) -> None: ...
    def relabeled_clone(self, relabels: dict[str, str]) -> Self: ...  # type: ignore[override]
    def as_sql(self, compiler: SQLCompiler, connection: Incomplete) -> tuple[str, list[Incomplete]]: ...  # type: ignore[override]

class HStoreRef(F):
    key: str
    def __init__(self, name: str, key: str) -> None: ...
    def resolve_expression(  # type: ignore[override]
        self,
        query: Incomplete = ...,
        allow_joins: bool = ...,
        reuse: set[str] | None = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> HStoreColumn: ...

class DateTimeEpochColumn(Col): ...

class DateTimeEpoch(F):
    def resolve_expression(  # type: ignore[override]
        self,
        query: Incomplete = ...,
        allow_joins: bool = ...,
        reuse: set[str] | None = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> DateTimeEpochColumn: ...

def IsNotNone(*fields: str, default: Incomplete | None = None) -> Case: ...

class ExcludedCol(Expression):
    name: str
    def __init__(self, name: str) -> None: ...
