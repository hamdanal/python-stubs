from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from shapely._enum import ParamEnum
from shapely._ragged_array import from_ragged_array, to_ragged_array
from shapely._typing import ArrayLike, GeoArray, GeoArrayLikeSeq
from shapely.geometry.base import BaseGeometry

__all__ = ["from_geojson", "from_ragged_array", "from_wkb", "from_wkt", "to_geojson", "to_ragged_array", "to_wkb", "to_wkt"]

DecodingErrorOptions = ParamEnum("DecodingErrorOptions", {"ignore": 0, "warn": 1, "raise": 2})  # raise is a reserved keyword

class WKBFlavorOptions(ParamEnum):
    extended: int
    iso: int

@overload
def to_wkt(
    geometry: BaseGeometry,
    rounding_precision: int = 6,
    trim: bool = True,
    output_dimension: int = 3,
    old_3d: bool = False,
    **kwargs,
) -> str: ...
@overload
def to_wkt(
    geometry: GeoArrayLikeSeq,
    rounding_precision: int = 6,
    trim: bool = True,
    output_dimension: int = 3,
    old_3d: bool = False,
    **kwargs,
) -> NDArray[np.str_]: ...
@overload
def to_wkb(
    geometry: BaseGeometry,
    hex: Literal[False] = False,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> bytes: ...
@overload
def to_wkb(
    geometry: BaseGeometry,
    hex: Literal[True],
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> str: ...
@overload
def to_wkb(
    geometry: BaseGeometry,
    hex: bool,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> bytes | str: ...
@overload
def to_wkb(
    geometry: GeoArrayLikeSeq,
    hex: Literal[False] = False,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> NDArray[np.bytes_]: ...
@overload
def to_wkb(
    geometry: GeoArrayLikeSeq,
    hex: Literal[True],
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> NDArray[np.str_]: ...
@overload
def to_wkb(
    geometry: GeoArrayLikeSeq,
    hex: bool,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> NDArray[np.bytes_] | NDArray[np.str_]: ...
@overload
def to_geojson(geometry: BaseGeometry, indent: int | None = None, **kwargs) -> str: ...
@overload
def to_geojson(geometry: GeoArrayLikeSeq, indent: int | None = None, **kwargs) -> NDArray[np.str_]: ...
@overload
def from_wkt(geometry: str, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> BaseGeometry: ...
@overload
def from_wkt(geometry: ArrayLike[str], on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> GeoArray: ...
@overload
def from_wkb(geometry: str | bytes, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> BaseGeometry: ...
@overload
def from_wkb(
    geometry: ArrayLike[str] | ArrayLike[bytes], on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs
) -> GeoArray: ...
@overload
def from_geojson(geometry: str | bytes, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> BaseGeometry: ...
@overload
def from_geojson(
    geometry: ArrayLike[str] | ArrayLike[bytes], on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs
) -> GeoArray: ...
