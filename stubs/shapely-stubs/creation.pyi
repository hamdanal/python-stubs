from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal, SupportsIndex

import numpy as np
from numpy.typing import NDArray

from shapely._geometry import GeometryType
from shapely._typing import ArrayLike, OptGeoArrayLike
from shapely.prepared import PreparedGeometry

__all__ = [
    "points",
    "linestrings",
    "linearrings",
    "polygons",
    "multipoints",
    "multilinestrings",
    "multipolygons",
    "geometrycollections",
    "box",
    "prepare",
    "destroy_prepared",
    "empty",
]

def points(
    coords,
    y: Incomplete | None = None,
    z: Incomplete | None = None,
    indices: Incomplete | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs,
): ...
def linestrings(
    coords,
    y: Incomplete | None = None,
    z: Incomplete | None = None,
    indices: Incomplete | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs,
): ...
def linearrings(
    coords,
    y: Incomplete | None = None,
    z: Incomplete | None = None,
    indices: Incomplete | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs,
): ...
def polygons(
    geometries,
    holes: Incomplete | None = None,
    indices: Incomplete | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs,
): ...
def box(xmin, ymin, xmax, ymax, ccw: bool = True, **kwargs): ...
def multipoints(geometries, indices: Incomplete | None = None, out: NDArray[np.object_] | None = None, **kwargs): ...
def multilinestrings(geometries, indices: Incomplete | None = None, out: NDArray[np.object_] | None = None, **kwargs): ...
def multipolygons(geometries, indices: Incomplete | None = None, out: NDArray[np.object_] | None = None, **kwargs): ...
def geometrycollections(geometries, indices: Incomplete | None = None, out: NDArray[np.object_] | None = None, **kwargs): ...
def prepare(geometry, **kwargs) -> None: ...
def destroy_prepared(geometry: OptGeoArrayLike | ArrayLike[PreparedGeometry[Any]], **kwargs) -> None: ...
def empty(
    shape: SupportsIndex | Sequence[SupportsIndex], geom_type: GeometryType | int | None = None, order: Literal["C", "F"] = "C"
) -> NDArray[np.object_]: ...
