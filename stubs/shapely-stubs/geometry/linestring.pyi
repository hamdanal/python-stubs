from collections.abc import Iterable
from typing import Literal, SupportsFloat
from typing_extensions import Self, TypeAlias

from shapely._typing import ArrayLikeSeq
from shapely.constructive import BufferCapStyle, BufferJoinStyle
from shapely.geometry.base import BaseGeometry
from shapely.geometry.multilinestring import MultiLineString
from shapely.geometry.multipoint import MultiPoint
from shapely.geometry.point import Point
from shapely.geometry.polygon import Polygon

__all__ = ["LineString"]

_ConvertibleToLineString: TypeAlias = LineString | ArrayLikeSeq[float] | Iterable[Point | Iterable[SupportsFloat]]

class LineString(BaseGeometry):
    def __new__(self, coordinates: _ConvertibleToLineString | None = None) -> Self: ...
    def svg(self, scale_factor: float = 1.0, stroke_color: str | None = None, opacity: float | None = None) -> str: ...  # type: ignore[override]
    def offset_curve(
        self, distance: float, quad_segs: int = 16, join_style=..., mitre_limit: float = 5.0
    ) -> LineString | MultiLineString: ...
    def parallel_offset(  # to be deprecated
        self, distance: float, side: str = "right", resolution: int = 16, join_style=..., mitre_limit: float = 5.0
    ) -> LineString | MultiLineString: ...
    # more precise base overrides
    @property
    def boundary(self) -> MultiPoint: ...  # empty geometry collection
    @property
    def convex_hull(self) -> LineString: ...
    @property
    def envelope(self) -> Polygon: ...
    @property
    def oriented_envelope(self) -> LineString: ...
    @property
    def minimum_rotated_rectangle(self) -> LineString: ...
    def buffer(
        self,
        distance: float,
        quad_segs: int = 16,
        cap_style: BufferCapStyle | Literal["round", "square", "flat"] = "round",
        join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
        mitre_limit: float = 5.0,
        single_sided: bool = False,
        *,
        quadsegs: int | None = None,  # deprecated
        resolution: int | None = None,  # to be deprecated
    ) -> Polygon: ...
