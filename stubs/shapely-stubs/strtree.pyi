from typing import SupportsIndex

from shapely._enum import ParamEnum
from shapely._typing import ArrayLike, GeoArray, GeoArrayLike, GeoArrayLikeSeq

__all__ = ["STRtree"]

class BinaryPredicate(ParamEnum):
    intersects: int
    within: int
    contains: int
    overlaps: int
    crosses: int
    touches: int
    covers: int
    covered_by: int
    contains_properly: int

class STRtree:
    def __init__(self, geoms: GeoArrayLikeSeq, node_capacity: SupportsIndex = 10) -> None: ...
    def __len__(self) -> int: ...
    @property
    def geometries(self) -> GeoArray: ...
    def query(
        self, geometry: GeoArrayLike, predicate: str | None = None, distance: ArrayLike[float] | None = None
    ): ...  # -> int | NDArray[np.int64]
    def nearest(self, geometry: GeoArrayLike): ...  # -> int | NDArray[np.int64] | None
    def query_nearest(
        self,
        geometry: GeoArrayLike,
        max_distance: float | None = None,
        return_distance: bool = False,
        exclusive: bool = False,
        all_matches: bool = True,
    ): ...  # very complex return type
