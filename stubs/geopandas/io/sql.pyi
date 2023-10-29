import sqlite3
from collections.abc import Generator, Mapping
from typing import Any, overload
from typing_extensions import TypeAlias

from geopandas import GeoDataFrame as GeoDataFrame
from pandas._typing import Scalar
from sqlalchemy.engine import Connectable

from ..base import _ConvertibleToCRS

_SQLConnection: TypeAlias = str | Connectable | sqlite3.Connection  # coppied from pandas.io.sql

@overload
def _read_postgis(
    sql: str,
    con: _SQLConnection,
    geom_col: str = "geom",
    crs: _ConvertibleToCRS | None = None,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = None,
    params: list[Scalar] | tuple[Scalar, ...] | Mapping[str, Scalar] | None = None,
    *,
    chunksize: int,
) -> Generator[GeoDataFrame, None, None]: ...
@overload
def _read_postgis(
    sql: str,
    con: _SQLConnection,
    geom_col: str = "geom",
    crs: _ConvertibleToCRS | None = None,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = None,
    params: list[Scalar] | tuple[Scalar, ...] | Mapping[str, Scalar] | None = None,
    chunksize: None = None,
) -> GeoDataFrame: ...

read_postgis = _read_postgis  # deprecated
