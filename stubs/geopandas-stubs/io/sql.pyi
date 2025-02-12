import sqlite3
from _typeshed import SupportsLenAndGetItem
from collections.abc import Container, Iterator, Mapping
from contextlib import AbstractContextManager
from typing import Any, Protocol, overload
from typing_extensions import TypeAlias

from pandas._typing import Scalar

from geopandas import GeoDataFrame
from geopandas.base import _ConvertibleToCRS

# Start SQLAlchemy hack
# ---------------------
# The code actually explicitly checks for SQLAlchemy's `Connection` and `Engine` with
# isinstance checks. However to avoid a dependency on SQLAlchemy, we use "good-enough"
# protocols that match as much as possible the SQLAlchemy implementation. This makes it
# very hard for someone to pass in the wrong object.
class _SqlalchemyTransactionLike(Protocol):
    # is_active: bool
    # connection: _SqlalchemyConnectionLike
    # def __init__(self, connection: _SqlalchemyConnectionLike): ...
    # @property
    # def is_valid(self) -> bool: ...
    def close(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...

class _SqlAlchemyEventTarget(Protocol):
    dispatch: Any

class _SqlalchemyConnectionLike(_SqlAlchemyEventTarget, Protocol):
    engine: Any
    @property
    def closed(self) -> bool: ...
    @property
    def invalidated(self) -> bool: ...
    def __enter__(self) -> _SqlalchemyConnectionLike: ...  # noqa: PYI034
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...  # noqa: PYI036
    @property
    def info(self) -> dict[Any, Any]: ...
    def invalidate(self, exception: BaseException | None = None) -> None: ...
    def detach(self) -> None: ...
    def begin(self) -> _SqlalchemyTransactionLike: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def recover_twophase(self) -> list[Any]: ...
    def rollback_prepared(self, xid: Any, recover: bool = ...) -> None: ...
    def commit_prepared(self, xid: Any, recover: bool = ...) -> None: ...
    def in_transaction(self) -> bool: ...
    def in_nested_transaction(self) -> bool: ...
    def close(self) -> None: ...

class _SqlalchemyEngineLike(_SqlAlchemyEventTarget, Protocol):
    dialect: Any
    pool: Any
    url: Any
    hide_parameters: bool
    @property
    def engine(self) -> _SqlalchemyEngineLike: ...
    def clear_compiled_cache(self) -> None: ...
    def update_execution_options(self, **opt: Any) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def driver(self) -> str: ...
    def dispose(self, close: bool = True) -> None: ...
    def begin(self) -> AbstractContextManager[Any]: ...
    def connect(self) -> Any: ...

_SqlalchemyConnectableLike: TypeAlias = _SqlalchemyConnectionLike | _SqlalchemyEngineLike
# ---------------------
# End SQLAlchemy hack

_SQLConnection: TypeAlias = str | _SqlalchemyConnectableLike | sqlite3.Connection  # coppied from pandas.io.sql

@overload
def _read_postgis(
    sql: str,
    con: _SQLConnection,
    geom_col: str = "geom",
    crs: _ConvertibleToCRS | None = None,
    index_col: str | Container[str] | None = None,
    coerce_float: bool = True,
    parse_dates: Container[str | Mapping[str, Any]] | Mapping[str, str | Mapping[str, Any]] | None = None,
    params: SupportsLenAndGetItem[Scalar] | Mapping[str, Scalar] | None = None,
    *,
    chunksize: int,
) -> Iterator[GeoDataFrame]: ...
@overload
def _read_postgis(
    sql: str,
    con: _SQLConnection,
    geom_col: str = "geom",
    crs: _ConvertibleToCRS | None = None,
    index_col: str | Container[str] | None = None,
    coerce_float: bool = True,
    parse_dates: Container[str | Mapping[str, Any]] | Mapping[str, str | Mapping[str, Any]] | None = None,
    params: SupportsLenAndGetItem[Scalar] | Mapping[str, Scalar] | None = None,
    chunksize: None = None,
) -> GeoDataFrame: ...
@overload
def _read_postgis(
    sql: str,
    con: _SQLConnection,
    geom_col: str = "geom",
    crs: _ConvertibleToCRS | None = None,
    index_col: str | Container[str] | None = None,
    coerce_float: bool = True,
    parse_dates: Container[str | Mapping[str, Any]] | Mapping[str, str | Mapping[str, Any]] | None = None,
    params: SupportsLenAndGetItem[Scalar] | Mapping[str, Scalar] | None = None,
    chunksize: int | None = None,
) -> GeoDataFrame | Iterator[GeoDataFrame]: ...
