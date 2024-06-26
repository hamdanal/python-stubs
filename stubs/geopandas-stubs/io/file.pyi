import os
from _typeshed import SupportsRead
from collections import OrderedDict
from collections.abc import Sequence
from typing import Any, Literal, TypedDict, overload
from typing_extensions import TypeAlias

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from pandas._typing import Axes
from shapely import Geometry

from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

_BboxLike: TypeAlias = Sequence[float] | NDArray[np.floating[Any]] | Geometry | GeoDataFrame | GeoSeries
_MaskLike: TypeAlias = dict[str, Any] | Geometry | GeoDataFrame | GeoSeries

@overload
def _read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox: _BboxLike | None = None,
    mask: _MaskLike | None = None,
    columns: Axes | None = None,
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
    columns: Axes | None = None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: Literal[True],
    layer: int | str | None = None,
    encoding: str | None = None,
    **kwargs: Any,  # depends on engine
) -> pd.DataFrame: ...

class _Schema(TypedDict):
    geometry: str | list[str]
    properties: OrderedDict[str, str]

def infer_schema(df: GeoDataFrame) -> _Schema: ...
def _list_layers(filename: str | bytes | os.PathLike[str] | os.PathLike[bytes] | SupportsRead[Any]) -> pd.DataFrame: ...
