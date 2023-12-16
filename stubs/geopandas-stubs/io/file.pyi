import os
from _typeshed import SupportsRead, SupportsWrite
from collections.abc import Sequence
from typing import Any, Literal, overload
from typing_extensions import TypeAlias, deprecated

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from shapely.geometry.base import BaseGeometry

from geopandas.base import _ConvertibleToCRS
from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

_BboxLike: TypeAlias = Sequence[float] | NDArray[np.floating[Any]] | BaseGeometry | GeoDataFrame | GeoSeries
_MaskLike: TypeAlias = dict[str, Any] | BaseGeometry | GeoDataFrame | GeoSeries

@overload
def _read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox: _BboxLike | None = None,
    mask: _MaskLike | None = None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: Literal[False] = False,
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
def infer_schema(df: GeoDataFrame) -> dict[str, Any]: ...
