from collections.abc import Callable
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from shapely._typing import ArrayLike, GeoArray, GeoArrayLike, GeoArrayLikeSeq
from shapely.geometry.base import BaseGeometry

__all__ = ["transform", "count_coordinates", "get_coordinates", "set_coordinates"]

@overload
def transform(
    geometry: BaseGeometry, transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]], include_z: bool = False
) -> BaseGeometry: ...
@overload
def transform(
    geometry: GeoArrayLikeSeq, transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]], include_z: bool = False
) -> GeoArray: ...
def count_coordinates(geometry: GeoArrayLike | None) -> int: ...
@overload
def get_coordinates(
    geometry: GeoArrayLike, include_z: bool = False, return_index: Literal[False] = False
) -> NDArray[np.float64]: ...
@overload
def get_coordinates(
    geometry: GeoArrayLike, include_z: bool = False, *, return_index: Literal[True]
) -> tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    geometry: GeoArrayLike, include_z: bool, return_index: Literal[True]
) -> tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    geometry: GeoArrayLike, include_z: bool = False, *, return_index: bool
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    geometry: GeoArrayLike, include_z: bool, return_index: bool
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def set_coordinates(geometry: BaseGeometry, coordinates: ArrayLike[float]) -> BaseGeometry: ...
@overload
def set_coordinates(geometry: GeoArrayLikeSeq, coordinates: ArrayLike[float]) -> GeoArray: ...
