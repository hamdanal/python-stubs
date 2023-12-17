from collections.abc import Iterable
from typing import overload
from typing_extensions import Self, TypeAlias

from shapely._typing import ArrayLikeSeq
from shapely.geometry.base import BaseGeometry
from shapely.geometry.collection import GeometryCollection
from shapely.geometry.polygon import Polygon

__all__ = ["Point"]

_PointLike: TypeAlias = Point | Iterable[float] | ArrayLikeSeq[float]

class Point(BaseGeometry):
    @overload  # no args: empty point
    def __new__(self) -> Self: ...
    @overload  # one arg: (x, y[, z]) tuple or a Point instance
    def __new__(self, __coords: _PointLike) -> Self: ...
    @overload  # two args: (x, y) tuple
    def __new__(self, __x: float, __y: float) -> Self: ...
    @overload  # three args: (x, y, z) tuple
    def __new__(self, __x: float, __y: float, __z: float) -> Self: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...
    def svg(self, scale_factor: float = 1.0, fill_color: str | None = None, opacity: float | None = None) -> str: ...
    # more precise base overrides
    @property
    def boundary(self) -> GeometryCollection: ...  # empty geometry collection
    @property
    def convex_hull(self) -> Point: ...
    @property
    def envelope(self) -> Point: ...
    @property
    def oriented_envelope(self) -> Point: ...
    @property
    def minimum_rotated_rectangle(self) -> Point: ...
    def buffer(
        self,
        distance: float,
        quad_segs: int = 16,
        cap_style: str = "round",
        join_style: str = "round",
        mitre_limit: float = 5.0,
        single_sided: bool = False,
    ) -> Polygon: ...
