import os
from _typeshed import Incomplete, SupportsGetItem, SupportsRead, SupportsWrite
from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
from json import JSONEncoder
from typing import Any, Literal, Protocol, overload, type_check_only
from typing_extensions import Self, TypeAlias, deprecated

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from pandas._typing import AggFuncTypeFrame, AstypeArg, Axes, Axis, Dtype, GroupByObject, IndexLabel, ListLikeU, Scalar
from pyproj import CRS
from shapely import Geometry

from geopandas.array import GeometryArray
from geopandas.base import GeoPandasBase, _ConvertibleToCRS
from geopandas.explore import _explore
from geopandas.geoseries import GeoSeries
from geopandas.io.file import _BboxLike, _MaskLike
from geopandas.io.sql import _SQLConnection
from geopandas.plotting import GeoplotAccessor
from geopandas.tools.clip import _Mask as _ClipMask

# XXX: cannot use pd.Series[Geometry] because of pd.Series type variable bounds
_GeomSeq: TypeAlias = Sequence[Geometry] | NDArray[np.object_] | pd.Series[Any] | GeometryArray | GeoSeries
_GeomCol: TypeAlias = Hashable | _GeomSeq  # name of column or column values
_ConvertibleToDataFrame: TypeAlias = (
    ListLikeU | pd.DataFrame | dict[Any, Any] | Iterable[ListLikeU | tuple[Hashable, ListLikeU] | dict[Any, Any]]
)

@type_check_only
class _SupportsGeoInterface(Protocol):
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...

crs_mismatch_error: str

class GeoDataFrame(GeoPandasBase, pd.DataFrame):  # type: ignore[misc]
    # Override the weird annotation of DataFrame.__new__ in pandas-stubs
    @overload
    def __new__(
        cls,
        data: _ConvertibleToDataFrame | None = None,
        index: Axes | None = None,
        columns: Axes | None = None,
        dtype: Dtype | None = None,
        copy: bool | None = None,
        *,
        geometry: _GeomCol | None = None,
        crs: _ConvertibleToCRS | None = None,
    ) -> Self: ...
    @overload
    def __new__(
        cls,
        data: Scalar,
        index: Axes,
        columns: Axes,
        dtype: Dtype | None = None,
        copy: bool | None = None,
        *,
        geometry: _GeomCol | None = None,
        crs: _ConvertibleToCRS | None = None,
    ) -> Self: ...
    def __init__(
        self,
        data: _ConvertibleToDataFrame | None = None,
        index: Axes | None = None,
        columns: Axes | None = None,
        dtype: Dtype | None = None,
        copy: bool | None = None,
        *,
        geometry: _GeomCol | None = None,
        crs: _ConvertibleToCRS | None = None,
    ) -> None: ...
    def __setattr__(self, attr: str, val: Any) -> None: ...
    @property
    def geometry(self) -> GeoSeries: ...
    @geometry.setter
    def geometry(self, col: _GeomSeq) -> None: ...
    @overload
    def set_geometry(
        self, col: _GeomCol, drop: bool = False, inplace: Literal[False] = False, crs: _ConvertibleToCRS | None = None
    ) -> Self: ...
    @overload
    def set_geometry(
        self, col: _GeomCol, drop: bool = False, *, inplace: Literal[True], crs: _ConvertibleToCRS | None = None
    ) -> None: ...
    @overload
    def set_geometry(self, col: _GeomCol, drop: bool, inplace: Literal[True], crs: _ConvertibleToCRS | None = None) -> None: ...
    @overload
    def rename_geometry(self, col: Hashable, inplace: Literal[False] = False) -> Self: ...
    @overload
    def rename_geometry(self, col: Hashable, inplace: Literal[True]) -> None: ...
    @property
    def crs(self) -> CRS | None: ...
    @crs.setter
    def crs(self, value: _ConvertibleToCRS | None) -> None: ...
    @classmethod
    def from_dict(  # type: ignore[override]
        cls, data: Mapping[Hashable, Any], geometry: _GeomCol | None = None, crs: _ConvertibleToCRS | None = None, **kwargs
    ) -> Self: ...
    @classmethod
    def from_file(
        cls,
        filename: str | os.PathLike[str] | SupportsRead[Any],
        *,
        bbox: _BboxLike | None = None,
        mask: _MaskLike | None = None,
        rows: int | slice | None = None,
        engine: Literal["fiona", "pyogrio"] | None = None,
        ignore_geometry: Literal[False] = False,
        **kwargs,  # engine dependent
    ) -> Self: ...
    @classmethod
    def from_features(
        cls,
        features: (
            _SupportsGeoInterface
            | Mapping[str, _SupportsGeoInterface | SupportsGetItem[str, Any]]
            | Iterable[_SupportsGeoInterface | SupportsGetItem[str, Any]]
        ),
        crs: _ConvertibleToCRS | None = None,
        columns: Axes | None = None,
    ) -> Self: ...
    @overload
    @classmethod
    def from_postgis(
        cls,
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
    ) -> Iterator[GeoDataFrame]: ...
    @overload
    @classmethod
    def from_postgis(
        cls,
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
    def to_json(  # type: ignore[override]
        self,
        na: str = "null",
        show_bbox: bool = False,
        drop_id: bool = False,
        to_wgs84: bool = False,
        *,
        # json.dumps kwargs
        skipkeys: bool = False,
        ensure_ascii: bool = True,
        check_circular: bool = True,
        allow_nan: bool = True,
        cls: type[JSONEncoder] | None = None,
        indent: int | str | None = None,
        separators: tuple[str, str] | None = None,
        default: Callable[[Any], Any] | None = None,
        sort_keys: bool = False,
        **kwargs,
    ) -> str: ...
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...
    def iterfeatures(self, na: str = "null", show_bbox: bool = False, drop_id: bool = False) -> Iterator[dict[str, Any]]: ...
    def to_wkb(
        self,
        hex: bool = False,
        *,
        # shapely kwargs
        output_dimension: int = ...,
        byte_order: int = ...,
        include_srid: bool = ...,
        flavor: Literal["iso", "extended"] = ...,
        **kwargs,
    ) -> pd.DataFrame: ...
    def to_wkt(
        self,
        *,
        # shapely kwargs
        rounding_precision: int = ...,
        trim: bool = ...,
        output_dimension: int = ...,
        old_3d: bool = ...,
        **kwargs,
    ) -> pd.DataFrame: ...
    def to_parquet(  # type: ignore[override]
        self,
        path: str | os.PathLike[str] | SupportsWrite[Incomplete],
        index: bool | None = None,
        compression: Literal["snappy", "gzip", "brotli"] | None = "snappy",
        schema_version: str | None = None,
        *,
        engine: Literal["auto", "pyarrow"] = "auto",  # Only these engines are supported, unlike pandas
        **kwargs,
    ) -> None: ...
    def to_feather(
        self,
        path: str | os.PathLike[str] | SupportsWrite[Incomplete],
        index: bool | None = None,
        compression: Literal["zstd", "lz4", "uncompressed"] | None = None,
        schema_version: str | None = None,
        **kwargs,
    ) -> None: ...
    # Keep method to_file roughly in line with GeoSeries.to_file
    def to_file(
        self,
        # TODO verify SupportsWrite[Any] is correct and remove Incomplete
        filename: str | os.PathLike[str] | SupportsWrite[Any] | Incomplete,
        driver: str | None = None,
        schema: dict[str, Any] | None = None,
        index: bool | None = None,
        *,
        mode: Literal["w", "a"] = "w",
        crs: _ConvertibleToCRS | None = None,
        engine: Literal["fiona", "pyogrio"] | None = None,
        layer: int | str | None = None,
        encoding: str | None = None,
        overwrite: bool | Incomplete = ...,  # TODO can it be None? (accepted by fiona, not sure about pyogrio)
        **kwargs: Any,  # engine and driver dependent
    ) -> None: ...
    @overload
    def set_crs(
        self, crs: _ConvertibleToCRS, epsg: int | None = None, inplace: bool = False, allow_override: bool = False
    ) -> Self: ...
    @overload
    def set_crs(
        self, crs: _ConvertibleToCRS | None = None, *, epsg: int, inplace: bool = False, allow_override: bool = False
    ) -> Self: ...
    @overload
    def set_crs(self, crs: _ConvertibleToCRS | None, epsg: int, inplace: bool = False, allow_override: bool = False) -> Self: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS, epsg: int | None = None, inplace: Literal[False] = False) -> Self: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS | None = None, *, epsg: int, inplace: Literal[False] = False) -> Self: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS | None, epsg: int, inplace: Literal[False] = False) -> Self: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS, epsg: int | None = None, *, inplace: Literal[True]) -> None: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS, epsg: int | None, inplace: Literal[True]) -> None: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS | None = None, *, epsg: int, inplace: Literal[True]) -> None: ...
    @overload
    def to_crs(self, crs: _ConvertibleToCRS | None, epsg: int, inplace: Literal[True]) -> None: ...
    def estimate_utm_crs(self, datum_name: str = "WGS 84") -> CRS: ...
    # def __getitem__(self, key): ...
    # def __setitem__(self, key, value) -> None: ...
    def copy(self, deep: bool = True) -> Self: ...
    # def merge(self, *args, **kwargs) -> GeoDataFrame | pd.DataFrame: ...
    def apply(  # type: ignore[override]
        self,
        func: Callable[..., Incomplete],
        axis: Axis = 0,
        raw: bool = False,
        result_type: Literal["expand", "reduce", "broadcast"] | None = None,
        args: tuple[Any, ...] = (),
        *,
        by_row: Literal[False, "compat"] = "compat",
        engine: Literal["python", "numba"] = "python",
        engine_kwargs: dict[str, bool] | None = None,
        **kwargs,
    ) -> pd.DataFrame | pd.Series[Any]: ...
    def __finalize__(self, other, method: str | None = None, **kwargs) -> Self: ...
    def dissolve(
        self,
        by: GroupByObject | None = None,
        aggfunc: AggFuncTypeFrame = "first",
        as_index: bool = True,
        level: IndexLabel | None = None,
        sort: bool = True,
        observed: bool = False,
        dropna: bool = True,
        **kwargs,
    ) -> GeoDataFrame: ...
    def explode(self, column: IndexLabel | None = None, ignore_index: bool = False, index_parts: bool | None = None) -> Self: ...
    def astype(
        self,
        dtype: AstypeArg | Mapping[Any, Dtype] | pd.Series[Any],
        copy: bool | None = None,
        errors: Literal["ignore", "raise"] = "raise",
    ) -> GeoDataFrame | pd.DataFrame: ...
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
        con: _SQLConnection,
        schema: str | None = None,
        if_exists: Literal["fail", "replace", "append"] = "fail",
        index: bool = False,
        index_label: IndexLabel | None = None,
        chunksize: int | None = None,
        dtype: dict[Any, Incomplete] | None = None,
    ) -> None: ...
    @deprecated("'^' operator is deprecated. Use the `symmetric_difference` method instead.")
    def __xor__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("'|' operator is deprecated. Use the `union` method instead.")
    def __or__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("'&' operator is deprecated. Use the `intersection` method instead.")
    def __and__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("'-' operator is deprecated. Use the `difference` method instead.")
    def __sub__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @property
    def plot(self) -> GeoplotAccessor: ...
    explore = _explore
    def sjoin(
        self,
        df: GeoDataFrame,
        # *args, **kwargs passed to geopandas.sjoin
        how: str = "inner",
        predicate: str = "intersects",
        lsuffix: str = "left",
        rsuffix: str = "right",
    ) -> GeoDataFrame: ...
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
    def clip(self, mask: _ClipMask, keep_geom_type: bool = False) -> GeoDataFrame: ...  # type: ignore[override]
    def overlay(
        self, right: GeoDataFrame, how: str = "intersection", keep_geom_type: bool | None = None, make_valid: bool = True
    ) -> GeoDataFrame: ...
