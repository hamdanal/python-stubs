import os
from _typeshed import SupportsRead, SupportsWrite
from collections import OrderedDict
from collections.abc import Sequence
from typing import Any, Literal, TypedDict, overload
from typing_extensions import TypeAlias, deprecated

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from shapely import Geometry

from geopandas.base import _ConvertibleToCRS
from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

_BboxLike: TypeAlias = Sequence[float] | NDArray[np.floating[Any]] | Geometry | GeoDataFrame | GeoSeries
_MaskLike: TypeAlias = dict[str, Any] | Geometry | GeoDataFrame | GeoSeries

@overload
def _read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox: _BboxLike | None = None,
    mask: _MaskLike | None = None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: Literal[False] = False,
    layer: int | str | None = None,
    encoding: str | None = None,
    **kwargs: Any,  # depends on engine
) -> GeoDataFrame: ...
@overload
def _read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox: _BboxLike | None = None,
    mask: _MaskLike | None = None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: Literal[True],
    layer: int | str | None = None,
    encoding: str | None = None,
    **kwargs: Any,  # depends on engine
) -> pd.DataFrame: ...
@deprecated("Function `geopandas.io.read_file` is deprecated. Use function `geopandas.from_file()` instead.")
def read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox: _BboxLike | None = None,
    mask: _MaskLike | None = None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: bool,
    layer: int | str | None = None,
    encoding: str | None = None,
    **kwargs: Any,
) -> pd.DataFrame: ...
@deprecated("Function `geopandas.io.to_file` is deprecated. Use `GeoDataFrame.to_file()` or `GeoSeries.to_file()` instead.")
def to_file(
    df: GeoDataFrame,
    filename: str | os.PathLike[str] | SupportsWrite[Any],
    driver: str | None = None,
    schema: dict[str, Any] | None = None,
    index: bool | None = None,
    mode: Literal["w", "a"] = "w",
    crs: _ConvertibleToCRS | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    **kwargs: Any,  # depends on driver
) -> None: ...

class _Schema(TypedDict):
    geometry: str | list[str]
    properties: OrderedDict[str, str]

def infer_schema(df: GeoDataFrame) -> _Schema: ...
