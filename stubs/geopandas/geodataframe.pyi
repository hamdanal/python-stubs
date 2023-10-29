import os
from _typeshed import Incomplete
from collections.abc import Generator, Hashable, Mapping, Sequence
from typing import Any, Literal, overload
from typing_extensions import Self, TypeAlias

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from pandas._typing import Axes, ListLikeU, Scalar
from pyproj import CRS
from shapely.geometry.base import BaseGeometry
from sqlalchemy.engine.base import Connection, Engine

from .array import GeometryArray
from .base import GeoPandasBase, _ConvertibleToCRS
from .explore import _explore
from .geoseries import GeoSeries
from .plotting import GeoplotAccessor

_Geometry: TypeAlias = Hashable | Sequence[BaseGeometry] | NDArray[np.object_] | pd.Series[BaseGeometry] | GeometryArray

crs_mismatch_error: str

class GeoDataFrame(GeoPandasBase, pd.DataFrame):  # type: ignore[misc]
    def __init__(
        self,
        data: ListLikeU | None = None,
        *args,
        geometry: _Geometry | None = None,
        crs: _ConvertibleToCRS | None = None,
        **kwargs,
    ) -> None: ...
    def __setattr__(self, attr: str, val: Any) -> None: ...
    @property
    def geometry(self) -> GeoSeries: ...
    @geometry.setter
    def geometry(self, col: _Geometry) -> None: ...
    def set_geometry(self, col: _Geometry, drop: bool = False, inplace: bool = False, crs: _ConvertibleToCRS | None = None): ...
    def rename_geometry(self, col: Hashable, inplace: bool = False): ...
    @property
    def crs(self) -> CRS | None: ...
    @crs.setter
    def crs(self, value: _ConvertibleToCRS) -> None: ...
    @classmethod
    def from_dict(
        cls, data: Mapping[Hashable, Any], geometry: _Geometry | None = None, crs: _ConvertibleToCRS | None = None, **kwargs
    ) -> Self: ...  # type: ignore[override]
    @classmethod
    def from_file(cls, filename: Incomplete, **kwargs) -> Self: ...
    @classmethod
    def from_features(cls, features: Incomplete, crs: _ConvertibleToCRS | None = None, columns: Axes | None = None) -> Self: ...
    @overload
    @classmethod
    def from_postgis(
        cls,
        sql: str,
        con: Connection | Engine,
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
    @classmethod
    def from_postgis(
        cls,
        sql: str,
        con: Connection | Engine,
        geom_col: str = "geom",
        crs: _ConvertibleToCRS | None = None,
        index_col: str | list[str] | None = None,
        coerce_float: bool = True,
        parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = None,
        params: list[Scalar] | tuple[Scalar, ...] | Mapping[str, Scalar] | None = None,
        chunksize: None = None,
    ) -> GeoDataFrame: ...
    def to_json(  # type: ignore[override]
        self, na: str = "null", show_bbox: bool = False, drop_id: bool = False, to_wgs84: bool = False, **kwargs
    ) -> str: ...
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...
    def iterfeatures(
        self, na: str = "null", show_bbox: bool = False, drop_id: bool = False
    ) -> Generator[dict[str, Any], None, None]: ...
    def to_wkb(self, hex: bool = ..., **kwargs) -> pd.DataFrame: ...
    def to_wkt(self, **kwargs) -> pd.DataFrame: ...
    def to_parquet(
        self,
        path: str | os.PathLike[str],
        index: bool | None = None,
        compression: Literal["snappy", "gzip", "brotli"] | None = "snappy",
        schema_version: str | None = None,
        **kwargs,
    ) -> None: ...
    def to_feather(
        self,
        path: str | os.PathLike[str],
        index: bool | None = None,
        compression: Literal["zstd", "lz4", "uncompressed"] | None = None,
        schema_version: str | None = None,
        **kwargs,
    ) -> None: ...
    def to_file(
        self,
        filename: Incomplete,
        driver: str | None = None,
        schema: Incomplete | None = None,
        index: bool | None = None,
        **kwargs,
    ) -> None: ...
    def set_crs(
        self, crs: _ConvertibleToCRS | None = None, epsg: int | None = None, inplace: bool = False, allow_override: bool = False
    ) -> Self: ...
    def to_crs(self, crs: _ConvertibleToCRS | None = None, epsg: int | None = None, inplace: bool = False) -> Self | None: ...
    def estimate_utm_crs(self, datum_name: str = "WGS 84") -> CRS: ...
    # def __getitem__(self, key): ...
    # def __setitem__(self, key, value) -> None: ...
    def copy(self, deep: bool = True) -> Self: ...
    def merge(self, *args, **kwargs) -> GeoDataFrame | pd.DataFrame: ...
    def apply(self, func, axis: int = 0, raw: bool = False, result_type: Incomplete | None = None, args=(), **kwargs): ...
    def __finalize__(self, other, method: Incomplete | None = None, **kwargs) -> Self: ...
    def dissolve(
        self,
        by: Incomplete | None = None,
        aggfunc: str | Incomplete = "first",
        as_index: bool = True,
        level: Incomplete | None = None,
        sort: bool = True,
        observed: bool = False,
        dropna: bool = True,
        **kwargs,
    ) -> GeoDataFrame: ...
    def explode(
        self, column: Hashable | None = None, ignore_index: bool = False, index_parts: bool | None = None, **kwargs
    ) -> Self: ...
    def astype(self, dtype, copy: bool = True, errors: str = "raise", **kwargs) -> GeoDataFrame | pd.DataFrame: ...
    def convert_dtypes(
        self,
        infer_objects: bool = True,
        convert_string: bool = True,
        convert_integer: bool = True,
        convert_boolean: bool = True,
        convert_floating: bool = True,
        dtype_backend: Literal["pyarrow", "numpy_nullable"] = "numpy_nullable",
    ) -> GeoDataFrame: ...
    def to_postgis(
        self,
        name: str,
        con: Connection | Engine,
        schema: str | None = None,
        if_exists: str = "fail",
        index: bool = False,
        index_label: Incomplete | None = None,
        chunksize: int | None = None,
        dtype: Incomplete | None = None,
    ) -> None: ...
    def __xor__(self, other): ...  # deprecated
    def __or__(self, other): ...  # deprecated
    def __and__(self, other): ...  # deprecated
    def __sub__(self, other): ...  # deprecated
    plot: GeoplotAccessor
    explore = _explore
    def sjoin(self, df: GeoDataFrame, *args, **kwargs) -> GeoDataFrame: ...
    def sjoin_nearest(
        self,
        right: GeoDataFrame,
        how: str = "inner",
        max_distance: float | None = None,
        lsuffix: str = "left",
        rsuffix: str = "right",
        distance_col: str | None = None,
        exclusive: bool = False,
    ) -> GeoDataFrame: ...
    def clip(self, mask, keep_geom_type: bool = False) -> GeoDataFrame: ...
    def overlay(
        self, right: GeoDataFrame, how: str = "intersection", keep_geom_type: bool | None = None, make_valid: bool = True
    ) -> GeoDataFrame: ...
