import json
import os
from _typeshed import Incomplete, SupportsRead, SupportsWrite, Unused
from collections.abc import Callable, Hashable, Mapping, Sequence
from typing import Any, Literal, overload
from typing_extensions import Self, TypeAlias, deprecated

import pandas as pd
from numpy.typing import ArrayLike
from pandas._typing import Axes, AxisIndex, Dtype
from pandas.core.base import IndexOpsMixin
from pyproj import CRS
from shapely import Geometry
from shapely.geometry.base import BaseGeometry

from geopandas.array import GeometryArray
from geopandas.base import GeoPandasBase, _ConvertibleToCRS
from geopandas.explore import _explore_geoseries
from geopandas.io.file import _BboxLike, _MaskLike
from geopandas.plotting import plot_series
from geopandas.tools.clip import _Mask as _ClipMask

# XXX: cannot use IndexOpsMixin[Geometry] because of IndexOpsMixin type variable bounds
_GeoListLike: TypeAlias = ArrayLike | Sequence[Geometry] | IndexOpsMixin[Incomplete]
_ConvertibleToGeoSeries: TypeAlias = Geometry | Mapping[int, Geometry] | Mapping[str, Geometry] | _GeoListLike

class GeoSeries(GeoPandasBase, pd.Series[BaseGeometry]):  # type: ignore[type-var,misc]  # pyright: ignore[reportInvalidTypeArguments]
    crs: CRS
    # Override the weird annotation of Series.__new__ in pandas-stubs
    def __new__(
        self,
        data: _ConvertibleToGeoSeries | None = None,
        index: Axes | None = None,
        crs: _ConvertibleToCRS | None = None,
        *,
        dtype: Dtype | None = None,
        name: Hashable = None,
        copy: bool | None = None,
        fastpath: bool = False,
    ) -> Self: ...
    def __init__(
        self,
        data: _ConvertibleToGeoSeries | None = None,
        index: Axes | None = None,
        crs: _ConvertibleToCRS | None = None,
        *,
        dtype: Dtype | None = None,
        name: Hashable = None,
        copy: bool | None = None,
        fastpath: bool = False,
    ) -> None: ...
    @property
    def values(self) -> GeometryArray: ...
    @deprecated("Method `Series.append()` has been removed in pandas version '2.0'.")
    def append(self, *args: Any, **kwargs: Any) -> GeoSeries: ...
    @property
    def geometry(self) -> Self: ...
    @property
    def x(self) -> pd.Series[float]: ...
    @property
    def y(self) -> pd.Series[float]: ...
    @property
    def z(self) -> pd.Series[float]: ...
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
        **kwargs: Any,  # depends on engine
    ) -> GeoSeries: ...
    @classmethod
    def from_wkb(
        cls,
        data: ArrayLike,  # array-like of bytes handled by shapely.from_wkb(data)
        index: Axes | None = None,
        crs: _ConvertibleToCRS | None = None,
        *,
        dtype: Dtype | None = None,
        name: Hashable = None,
        copy: bool | None = None,
        fastpath: bool = False,
    ) -> Self: ...
    @classmethod
    def from_wkt(
        cls,
        data: ArrayLike,  # array-like of str handled by shapely.from_wkt(data)
        index: Axes | None = None,
        crs: _ConvertibleToCRS | None = None,
        *,
        dtype: Dtype | None = None,
        name: Hashable = None,
        copy: bool | None = None,
        fastpath: bool = False,
    ) -> Self: ...
    @classmethod
    def from_xy(
        cls,
        # x, y, z: array-like of floats handled by np.asarray(..., dtype="float64")
        x: ArrayLike,
        y: ArrayLike,
        z: ArrayLike | None = None,
        index: Axes | None = None,
        crs: _ConvertibleToCRS | None = None,
        *,
        dtype: Dtype | None = None,
        name: Hashable = None,
        copy: bool | None = None,
        fastpath: bool = False,
    ) -> Self: ...
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...
    # Keep method to_file roughly in line with GeoDataFrame.to_file
    def to_file(
        self,
        filename: str | os.PathLike[str] | SupportsWrite[Any] | Incomplete,
        driver: str | None = None,
        index: bool | None = None,
        *,
        schema: dict[str, Any] | None = None,
        mode: Literal["w", "a"] = "w",
        crs: _ConvertibleToCRS | None = None,
        engine: Literal["fiona", "pyogrio"] | None = None,
        **kwargs: Any,  # depends on driver
    ) -> None: ...
    # *** TODO: compare `__getitem__` with pandas-stubs ***
    # def __getitem__(self, key): ...
    # *** `sort_index` is annotated with `-> Self` in pandas-stubs; no need to override it ***
    # def sort_index(self, *args, **kwargs): ...
    def take(self, indices: ArrayLike, axis: AxisIndex = 0, **kwargs: Unused) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("Method `Series.select()` has been removed in pandas version '0.25'.")
    def select(self, *args: Any, **kwargs: Any) -> Any: ...
    # *** `apply` annotation in pandas-stubs is compatible except for deprecated `convert_dtype` argument ***
    # def apply(self, func, convert_dtype: bool | None = None, args=(), **kwargs): ...
    def isna(self) -> pd.Series[bool]: ...
    def isnull(self) -> pd.Series[bool]: ...
    def notna(self) -> pd.Series[bool]: ...
    def notnull(self) -> pd.Series[bool]: ...
    # *** TODO: `fillna` annotation in pandas-stubs is NOT compatible; must `-> Self` ***
    # def fillna(self, value=None, method: FillnaOptions | None = None, inplace: bool = False, **kwargs): ...
    def __contains__(self, other: object) -> bool: ...
    plot = plot_series  # type: ignore[assignment] # pyright: ignore
    explore = _explore_geoseries
    def explode(self, ignore_index: bool = False, index_parts: bool | None = None) -> GeoSeries: ...
    def set_crs(
        self, crs: _ConvertibleToCRS | None = None, epsg: int | None = None, inplace: bool = False, allow_override: bool = False
    ) -> Self: ...
    def to_crs(self, crs: _ConvertibleToCRS | None = None, epsg: int | None = None) -> GeoSeries: ...
    def estimate_utm_crs(self, datum_name: str = "WGS 84") -> CRS: ...
    def to_json(  # type: ignore[override]
        self,
        *,
        # Keywords from json.dumps
        skipkeys: bool = False,
        ensure_ascii: bool = True,
        check_circular: bool = True,
        allow_nan: bool = True,
        cls: type[json.JSONEncoder] | None = None,
        indent: None | int | str = None,
        separators: tuple[str, str] | None = None,
        default: Callable[[Any], Any] | None = None,
        sort_keys: bool = False,
        **kwds: Any,
    ) -> str: ...
    @overload
    def to_wkb(self, hex: Literal[False] = False, **kwargs) -> pd.Series[bytes]: ...
    @overload
    def to_wkb(self, hex: Literal[True], **kwargs) -> pd.Series[str]: ...
    @overload
    def to_wkb(self, hex: bool = False, **kwargs) -> pd.Series[str] | pd.Series[bytes]: ...
    def to_wkt(self, **kwargs) -> pd.Series[str]: ...
    @deprecated("'^' operator is deprecated. Use method `symmetric_difference` instead.")
    def __xor__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("'|' operator is deprecated. Use method `union` instead.")
    def __or__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("'&' operator is deprecated. Use method `intersection` instead.")
    def __and__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    @deprecated("'-' operator is deprecated. Use method `difference` instead.")
    def __sub__(self, other: GeoSeries | Geometry) -> GeoSeries: ...  # type: ignore[override]
    def clip(self, mask: _ClipMask, keep_geom_type: bool = False) -> GeoSeries: ...  # type: ignore[override]
