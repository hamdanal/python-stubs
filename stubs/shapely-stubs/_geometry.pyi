from enum import IntEnum
from typing import overload

import numpy as np
from numpy.typing import NDArray

from shapely._enum import ParamEnum
from shapely._typing import ArrayLike, GeoArrayLikeSeq
from shapely.geometry.base import BaseGeometry

__all__ = [
    "GeometryType",
    "get_type_id",
    "get_dimensions",
    "get_coordinate_dimension",
    "get_num_coordinates",
    "get_srid",
    "set_srid",
    "get_x",
    "get_y",
    "get_z",
    "get_exterior_ring",
    "get_num_points",
    "get_num_interior_rings",
    "get_num_geometries",
    "get_point",
    "get_interior_ring",
    "get_geometry",
    "get_parts",
    "get_rings",
    "get_precision",
    "set_precision",
    "force_2d",
    "force_3d",
]

class GeometryType(IntEnum):
    MISSING: int
    POINT: int
    LINESTRING: int
    LINEARRING: int
    POLYGON: int
    MULTIPOINT: int
    MULTILINESTRING: int
    MULTIPOLYGON: int
    GEOMETRYCOLLECTION: int

@overload
def get_type_id(geometry: BaseGeometry | None, **kwargs) -> int: ...
@overload
def get_type_id(geometry: GeoArrayLikeSeq, **kwargs) -> NDArray[np.int_]: ...
def get_dimensions(geometry, **kwargs): ...
def get_coordinate_dimension(geometry, **kwargs): ...
def get_num_coordinates(geometry, **kwargs): ...
def get_srid(geometry, **kwargs): ...
def set_srid(geometry, srid, **kwargs): ...
def get_x(point, **kwargs): ...
def get_y(point, **kwargs): ...
def get_z(point, **kwargs): ...
def get_point(geometry, index, **kwargs): ...
def get_num_points(geometry, **kwargs): ...
def get_exterior_ring(geometry, **kwargs): ...
def get_interior_ring(geometry, index, **kwargs): ...
def get_num_interior_rings(geometry, **kwargs): ...
def get_geometry(geometry, index, **kwargs): ...
def get_parts(geometry, return_index: bool = False): ...
def get_rings(geometry, return_index: bool = False): ...
def get_num_geometries(geometry, **kwargs): ...
def get_precision(geometry, **kwargs): ...

class SetPrecisionMode(ParamEnum):
    valid_output: int
    pointwise: int
    keep_collapsed: int

def set_precision(geometry, grid_size: float, mode: str = "valid_output", **kwargs): ...
def force_2d(geometry, **kwargs): ...
def force_3d(geometry, z: ArrayLike[float] = 0.0, **kwargs): ...
