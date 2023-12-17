import numpy as np
from numpy.typing import ArrayLike, NDArray

from shapely._geometry import GeometryType

def to_ragged_array(
    geometries: ArrayLike, include_z: bool | None = None
) -> tuple[GeometryType, NDArray[np.float64], tuple[NDArray[np.int_], ...]]: ...
def from_ragged_array(
    geometry_type: GeometryType, coords: ArrayLike, offsets: tuple[ArrayLike, ...] | None = None
) -> NDArray[np.object_]: ...
